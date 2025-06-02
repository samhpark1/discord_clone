from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.db import Base

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    server_id: Mapped[int] = mapped_column(ForeignKey("servers.id"))
