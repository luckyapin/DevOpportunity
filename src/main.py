import aioredis
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from src.upload.router import router as router_upload

app = FastAPI(
    title='DevOpportunity'
)

app.include_router(
    router_upload
)

@app.on_event('startup')
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding='utf8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')