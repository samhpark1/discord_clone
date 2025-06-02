from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.db import Base

class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    edited: Mapped[bool] = mapped_column(default=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    channel_id: Mapped[int] = mapped_column(ForeignKey("channels.id"))

    author = relationship("User", back_populates="messages")
    channel = relationship("Channel", back_populates="messages")
    attachments = relationship("Attachment", back_populates="message")
