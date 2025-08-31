from fastapi import FastAPI

from api import router as api_router

from core.config import settings

import uvicorn

app = FastAPI()
app.include_router(
    api_router,
    prefix=settings.api.prefix
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
