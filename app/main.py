import logging

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api import router as api_router

from core.config import settings

from core.models import db_helper

from middlewares import register_middlewares

import uvicorn
import sys


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


def create_app() -> FastAPI:
    app = FastAPI(
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
    )

    app.include_router(
        api_router,
        prefix=settings.api.prefix,
    )
    
    register_middlewares(app)

    return app


if __name__ == "__main__":
    uvicorn.run(
        "main:create_app",
        host=settings.run.host,
        port=settings.run.port,
        factory=True,
        reload=True
    )
