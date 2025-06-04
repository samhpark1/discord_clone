from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
from dotenv import load_dotenv
import os
import logging

load_dotenv()

class SQLManager:
    def __init__(self, db_uri=None):
        self.db_uri = db_uri or os.getenv("SQL_URL")
        self.engine = create_engine(self.db_uri, echo=True, future=True)
        self.SessionLocal = scoped_session(sessionmaker(bind=self.engine))

    def get_session(self):
        return self.SessionLocal()
    
    def close(self):
        self.SessionLocal.remove()

    def init_db(self, Base):
        Base.metadata.create_all(bind=self.engine)

    