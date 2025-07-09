import asyncio
import html
import logging

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from social_media_agent.basemodel import BaseNode, OverallState
from social_media_agent.configs.logging_config import setup_logging
from html_to_markdown import convert_to_markdown

setup_logging()
logger = logging.getLogger(__name__)


class ScraperNode(BaseNode):
    """
    Scraper node that extracts HTML content from a user-supplied URL using crawl4ai
    and converts it to Markdown for downstream processing.
    """

    async def run_async(self, state: OverallState) -> OverallState:
        url = state.get("url")
        js_commands = [
            "window.scrollTo(0, document.body.scrollHeight);",
            "document.querySelector('a.morelink')?.click();"
        ]
        config = CrawlerRunConfig(js_code=js_commands)

        try:
            async with AsyncWebCrawler() as crawler:
                result = await crawler.arun(url=url, config=config)

            html_content = html.unescape(result.cleaned_html)

            markdown_content = convert_to_markdown(html_content)

            logger.info(f"[ScraperNode] Scraped {len(html_content)} characters and converted to Markdown.")

            logger.info(f"[ScraperNode] Markdown preview:\n{markdown_content[:500]}...")

            state["content"] = markdown_content

        except Exception as e:
            logger.error(f"[ScraperNode] Failed to scrape {url}: {e}")
            state["content"] = ""

        return state

    async def run(self, state: OverallState) -> OverallState:
        return await self.run_async(state)
