from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.db import Base
from app.tables.channel_type import ChannelType

class Channel(Base):
    __tablename__ = "channels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    type: Mapped[ChannelType]
    server_id: Mapped[int] = mapped_column(ForeignKey("servers.id"))
    parent_id: Mapped[int] = mapped_column(ForeignKey("channels.id"), nullable=True)

    server = relationship("Server", back_populates="channels")
    messages = relationship("Message", back_populates="channel")
