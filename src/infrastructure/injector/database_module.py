import os

from dotenv import load_dotenv
from injector import Module, provider, singleton
from sqlalchemy import Engine, create_engine

load_dotenv()


class DatabaseModule(Module):
    path = os.getenv("DB_URL", "postgresql://dbuser:dbpassword@localhost:5432/python_template")

    @singleton
    @provider
    def database(self) -> Engine:
        return create_engine(self.path)
