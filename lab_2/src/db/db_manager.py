from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from src.db.settings import DATABASE_URL
from src.db.models.clinic import Base, ClinicInfoBase
from datetime import date


class DatabaseManager:
    def __init__(self, db_url: str = DATABASE_URL) -> None:
        self.__engine = create_engine(db_url)
        self.__session_local = sessionmaker(bind=self.__engine)

    def create_tables(self) -> None:
        Base.metadata.create_all(self.__engine)

    @property
    def session(self) -> Session:
        return self.__session_local()
