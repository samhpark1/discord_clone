from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.db import Base

class Attachment(Base):
    __tablename__ = "attachments"

    id: Mapped[int] = mapped_column(primary_key=True)
    message_id: Mapped[int] = mapped_column(ForeignKey("messages.id"))
    file_url: Mapped[str]
    file_type: Mapped[str]
    size: Mapped[int]

    message = relationship("Message", back_populates="attachments")
