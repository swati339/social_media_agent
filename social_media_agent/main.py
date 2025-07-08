from fastapi import FastAPI
from social_media_agent.routes.social_media_pipeline import router  
app = FastAPI(
    title="Social Media Agent API",
    version="1.0.0"
)

app.include_router(router)
