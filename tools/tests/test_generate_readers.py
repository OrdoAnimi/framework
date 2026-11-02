"""Tests for reader-page dates: real publication dates override the git date."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import generate_readers as g


def test_publish_date_prefers_the_recorded_date(monkeypatch):
    monkeypatch.setattr(g, "_PUBLISH_DATES", {"a.md": "2026-11-01"})
    monkeypatch.setattr(g, "first_commit_date", lambda p: "2026-06-05")
    assert g.publish_date("a.md") == "2026-11-01"


def test_publish_date_null_means_no_date_shown(monkeypatch):
    monkeypatch.setattr(g, "_PUBLISH_DATES", {"a.md": None})
    monkeypatch.setattr(g, "first_commit_date", lambda p: "2026-06-05")
    assert g.publish_date("a.md") == ""


def test_publish_date_falls_back_to_git(monkeypatch):
    monkeypatch.setattr(g, "_PUBLISH_DATES", {})
    monkeypatch.setattr(g, "first_commit_date", lambda p: "2026-06-05")
    assert g.publish_date("a.md") == "2026-06-05"
