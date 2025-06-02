from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.db import Base

class Membership(Base):
    __tablename__ = "memberships"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    server_id: Mapped[int] = mapped_column(ForeignKey("servers.id"), primary_key=True)
    joined_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    user = relationship("User")
    server = relationship("Server", back_populates="members")
