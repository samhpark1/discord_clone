from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    avatar: Mapped[str] = mapped_column(nullable=True)
    password_hash: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    messages = relationship("Message", back_populates="author")



    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"