from app.db.db_manager import DBManager
from sqlalchemy.orm import declarative_base

Base = declarative_base()

db_manager = DBManager()
db_manager.sql.init_db(Base)