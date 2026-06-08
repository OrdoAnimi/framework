import sys, os, tempfile, shutil, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from tools.generate_pages import extract_meta, derive_eyebrow, render_research_page, render_publications_page, update_sidebar


class TestExtractMeta(unittest.TestCase):
    def test_h1_title(self):
        content = "# My Title\n## My Subtitle\n\n**Date:** May 2026\n"
        m = extract_meta(content, "my-paper-may-2026.md")
        self.assertEqual(m['title'], 'My Title')

    def test_h2_description(self):
        content = "# Title\n## The Subtitle Here\n"
        m = extract_meta(content, "foo.md")
        self.assertEqual(m['description'], 'The Subtitle Here')

    def test_date_extraction(self):
        content = "# T\n\n**Date:** June 2026\n"
        m = extract_meta(content, "foo.md")
        self.assertEqual(m['date'], 'June 2026')

    def test_slug_from_filename(self):
        content = "# T\n"
        m = extract_meta(content, "my-new-paper-june-2026.md")
        self.assertEqual(m['slug'], 'my-new-paper-june-2026')

    def test_title_fallback_from_slug(self):
        content = "no heading here\n"
        m = extract_meta(content, "my-slug.md")
        self.assertNotEqual(m['title'], '')


class TestDeriveEyebrow(unittest.TestCase):
    def test_addendum(self):
        self.assertIn('Addendum', derive_eyebrow('foo-addendum-may-2026', 'May 2026'))

    def test_working_paper(self):
        self.assertIn('Working Paper', derive_eyebrow('zencloud-governance-june-2026', 'June 2026'))

    def test_series(self):
        self.assertIn('Research Series', derive_eyebrow('05-new-topic', ''))

    def test_extended(self):
        self.assertIn('Extended', derive_eyebrow('EA-New-Analysis', ''))


class TestRenderPages(unittest.TestCase):
    def _meta(self, slug='test-paper-may-2026', title='Test Title', desc='Test desc', date='May 2026'):
        return {'title': title, 'description': desc, 'eyebrow': 'Working Paper · May 2026',
                'slug': slug, 'filename': slug + '.md', 'date': date}

    def test_research_page_contains_title(self):
        html = render_research_page(self._meta())
        self.assertIn('Test Title', html)

    def test_research_page_contains_raw_src(self):
        html = render_research_page(self._meta())
        self.assertIn('raw.githubusercontent.com', html)
        self.assertIn('test-paper-may-2026.md', html)

    def test_research_page_back_link(self):
        html = render_research_page(self._meta())
        self.assertIn('../../research/', html)

    def test_publications_page_back_link(self):
        html = render_publications_page(self._meta())
        self.assertIn('../../publications/', html)

    def test_publications_page_contains_title(self):
        html = render_publications_page(self._meta())
        self.assertIn('Test Title', html)


class TestUpdateSidebar(unittest.TestCase):
    def test_inserts_before_marker(self):
        html = '<div>existing</button><!-- AUTO-PAPERS --></div>'
        result = update_sidebar(html, '<!-- AUTO-PAPERS -->', '<button>New</button>')
        self.assertIn('<button>New</button><!-- AUTO-PAPERS -->', result)
        self.assertIn('existing', result)

    def test_no_marker_returns_unchanged(self):
        html = '<div>no marker here</div>'
        result = update_sidebar(html, '<!-- AUTO-PAPERS -->', '<button>New</button>')
        self.assertEqual(result, html)

    def test_idempotent_existing_entry(self):
        btn = '<button data-p="research/foo.md">Foo</button>'
        html = f'{btn}<!-- AUTO-PAPERS --></div>'
        result = update_sidebar(html, '<!-- AUTO-PAPERS -->', btn)
        self.assertEqual(result.count(btn), 1)


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.research = os.path.join(self.tmp, 'research')
        os.makedirs(self.research)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_generates_subfolder_for_new_md(self):
        md = os.path.join(self.research, 'new-article-june-2026.md')
        with open(md, 'w') as f:
            f.write("# New Article\n## A subtitle\n\n**Date:** June 2026\n")

        from tools.generate_pages import process_directory
        process_directory(self.research, 'research', self.tmp)

        target = os.path.join(self.research, 'new-article-june-2026', 'index.html')
        self.assertTrue(os.path.exists(target))
        content = open(target).read()
        self.assertIn('New Article', content)
        self.assertIn('new-article-june-2026.md', content)

    def test_skips_existing_subfolder(self):
        md = os.path.join(self.research, 'existing.md')
        with open(md, 'w') as f:
            f.write("# Existing\n")
        subfolder = os.path.join(self.research, 'existing')
        os.makedirs(subfolder)
        sentinel = os.path.join(subfolder, 'index.html')
        with open(sentinel, 'w') as f:
            f.write('ORIGINAL')

        from tools.generate_pages import process_directory
        process_directory(self.research, 'research', self.tmp)

        self.assertEqual(open(sentinel).read(), 'ORIGINAL')

    def test_skips_excluded_files(self):
        for name in ['SOURCES.md', 'PUBLISHING.md', 'README.md']:
            with open(os.path.join(self.research, name), 'w') as f:
                f.write("# Skip me\n")

        from tools.generate_pages import process_directory
        generated = process_directory(self.research, 'research', self.tmp)
        self.assertEqual(generated, [])


if __name__ == '__main__':
    unittest.main()
