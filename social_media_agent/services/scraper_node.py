import asyncio
import html
import logging
from urllib.parse import urljoin

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from social_media_agent.basemodel import BaseNode, OverallState
from social_media_agent.configs.logging_config import setup_logging
from html_to_markdown import convert_to_markdown

setup_logging()
logger = logging.getLogger(__name__)

class ScraperNode(BaseNode):
    async def run_async(self, state: OverallState) -> OverallState:
        url = state["url"]
        js_commands = [
            "window.scrollTo(0, document.body.scrollHeight);",
            "document.querySelector('a.morelink')?.click();"
        ]

        config = CrawlerRunConfig(
            js_code=js_commands,
            wait_for_images=True,
            scan_full_page=True,
            scroll_delay=0.5,
        )

        try:
            async with AsyncWebCrawler() as crawler:
                result = await crawler.arun(url=url, config=config)

            html_content = html.unescape(result.cleaned_html)
            markdown_content = convert_to_markdown(html_content)

            image_url = None
            if result.media:
                logger.debug(f"[ScraperNode] Media items: {result.media}")
                for media_item in result.media:
                    if isinstance(media_item, str) and media_item.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                        image_url = urljoin(url, media_item)
                        break

            logger.info(f"[ScraperNode] Scraped {len(html_content)} chars.")
            logger.info(f"[ScraperNode] Extracted image URL: {image_url}")

            state["content"] = markdown_content
            state["image_url"] = image_url

        except Exception as e:
            logger.error(f"[ScraperNode] Failed to scrape {url}: {e}")
            state["content"] = ""
            state["image_url"] = None

        return state

    async def run(self, state: OverallState) -> OverallState:
        return await self.run_async(state)


