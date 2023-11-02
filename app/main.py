from fastapi import FastAPI

from app.routers import (
    chatgpt,
    vector,
)

from app.version import __version__


app = FastAPI(
    title="API ChatGPT T-Rex",
    description="Demo API chat GPT with own data.",
    version=__version__,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.include_router(chatgpt.router)
app.include_router(vector.router)