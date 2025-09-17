## Social Media Agent

🚀 An AI-powered social media automation agent built with FastAPI, LangChain, LangGraph, Crawl4AI, and Tweepy.
It can crawl content from the web, generate insights or posts using AI, and publish directly to Twitter/X.

## Features

🌐 Web Crawling – Extract structured data from websites using Crawl4AI.

🧠 AI-Powered Text Generation – Leverage LangChain+ LangGraph for intelligent post generation.

🐦 Twitter/X Integration – Automate posting, replying, and engagement via Tweepy.

⚡ API-First Design – Built on FastAPIfor easy integration with other apps.

🛠️ Configurable & Extensible – Add your own logic, workflows, or social media platforms.


## Installation

Clone the repository and install dependencies using uv (recommended) or pip.

``` bash
git clone https://github.com/swati339/social-media-agent.git
cd social-media-agent
uv sync
```

## Configuration

Set up your .env file with API keys and tokens:

``` bash
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
OPENAI_API_KEY=your_openai_key
```

```bash
uv sync
```

## Usage
Start your fastapi with:
```bash
uvicorn social_media_agent.main:app 
```

Then open http://localhost:8000/docs
 to explore API endpoints.

## Example Workflows

Crawl & Post: Crawl trending content, summarize it, and post automatically.

Engagement Bot: Auto-reply to mentions with AI-generated responses.

Content Planner: Schedule posts with generated hashtags & captions.



