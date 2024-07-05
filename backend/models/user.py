from sqlalchemy.orm import Mapped, mapped_column
from db import db

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)

    def __repr__(self):
        return f'<User {self.username}>'