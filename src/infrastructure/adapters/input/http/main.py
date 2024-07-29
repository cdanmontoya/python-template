import os

import uvicorn
from dotenv import load_dotenv

from src.infrastructure.adapters.input.http.application import Application
from src.infrastructure.injector.injector import create_injector

app = Application(create_injector()).create_app()


if __name__ == "__main__":
    load_dotenv()

    uvicorn.run(
        "src.infrastructure.adapters.input.http.main:app",
        port=int(os.getenv("APP_PORT", 8080)),
        host="0.0.0.0",
        reload=True,
    )