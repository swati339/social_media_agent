import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from social_media_agent.basemodel import BaseNode, OverallState
from social_media_agent.configs.logging_config import setup_logging
import logging

setup_logging()

logger = logging.getLogger(__name__)

class ScraperNode(BaseNode):
    """
    Scraper node that extracts HTML content from a user-supplied URL using crawl4ai.
    """

    async def run_async(self, state: OverallState) -> OverallState:
        url = state["url"]
        js_commands = [
            "window.scrollTo(0, document.body.scrollHeight);",
            "document.querySelector('a.morelink')?.click();"
        ]
        config = CrawlerRunConfig(js_code=js_commands)

        try:
            async with AsyncWebCrawler() as crawler:
                result = await crawler.arun(url=url, config=config)

            content = result.cleaned_html
            logger.info(f"[ScraperNode] Scraped {len(content)} characters from {url}")
            state["content"] = content

        except Exception as e:
            logger.info(f"[ScraperNode] Failed to scrape {url}: {e}")
            state["content"] = ""

        return state

    async def run(self, state: OverallState) -> OverallState:
        return await self.run_async(state)


# if __name__ == "__main__":
#     url = input("Enter the URL to scrape: ").strip()
#     state = {"url": url}
#     node = ScraperNode()
#     result = node.run(state)

#     logger.info("\nScraped HTML preview:")
#     logger.info(result["content"][:1000])
