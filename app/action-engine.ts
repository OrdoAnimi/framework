import axios from 'axios';
import { Artefact } from './types/index';
import { logger } from './logger';

class ActionEngine {
  private githubToken = process.env.VAF_GITHUB_TOKEN;
  private owner = process.env.GITHUB_OWNER || 'ZenCloudAU';
  private repo = process.env.GITHUB_REPO || 'velocity-architecture';

  async commitArtefact(requestId: string, artefact: Artefact): Promise<{ sha: string; url: string }> {
    if (!this.githubToken) {
      throw new Error('VAF_GITHUB_TOKEN not configured');
    }

    const fileName = `artefacts/${artefact.type}/${requestId}-${artefact.type}.md`;
    const message = `[VAF v2] Generated ${artefact.type} artefact for ${requestId}`;
    const content = Buffer.from(artefact.content).toString('base64');

    try {
      // Pure function: direct GitHub API call (no LLM reasoning)
      const response = await axios.put(
        `https://api.github.com/repos/${this.owner}/${this.repo}/contents/${fileName}`,
        {
          message,
          content,
          branch: 'main',
          committer: {
            name: 'VAF Agentic Architect',
            email: 'vaf-agent@zencloud.com.au',
          },
        },
        {
          headers: {
            Authorization: `token ${this.githubToken}`,
            'Content-Type': 'application/json',
            Accept: 'application/vnd.github.v3+json',
          },
        }
      );

      logger.info(
        {
          requestId,
          type: artefact.type,
          sha: response.data.commit.sha,
          fileName,
        },
        'Artefact committed to GitHub'
      );

      return {
        sha: response.data.commit.sha,
        url: response.data.html_url,
      };
    } catch (error) {
      logger.error(
        {
          requestId,
          fileName,
          error: error instanceof Error ? error.message : String(error),
        },
        'Failed to commit artefact'
      );
      throw error;
    }
  }

  async getArtefact(id: string): Promise<Artefact | null> {
    if (!this.githubToken) {
      throw new Error('VAF_GITHUB_TOKEN not configured');
    }

    try {
      const response = await axios.get(
        `https://api.github.com/repos/${this.owner}/${this.repo}/contents/artefacts`,
        {
          headers: {
            Authorization: `token ${this.githubToken}`,
            Accept: 'application/vnd.github.v3+json',
          },
        }
      );

      const files = response.data as { name: string; path: string }[];
      const match = files.find(f => f.name.includes(id));
      if (!match) return null;

      const fileResponse = await axios.get(
        `https://api.github.com/repos/${this.owner}/${this.repo}/contents/${match.path}`,
        {
          headers: {
            Authorization: `token ${this.githubToken}`,
            Accept: 'application/vnd.github.v3.raw',
          },
        }
      );

      logger.info({ id }, 'Artefact retrieved from GitHub');
      return JSON.parse(fileResponse.data);
    } catch (error) {
      logger.debug({ id, error }, 'Artefact not found or retrieval failed');
      return null;
    }
  }
}

export const actionEngine = new ActionEngine();
