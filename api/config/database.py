import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Database:
    def __init__(self) -> None:
        self.__connection_string = os.environ.get('STRING_CONNECTION_MYSQL')
        self.__engine = create_engine(self.__connection_string)
        self.session = None

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        self.session = Session(self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
