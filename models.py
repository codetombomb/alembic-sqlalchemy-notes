from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birthday = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return (
            "<User\n"
            + f"id={self.id}\n"
            + f"first_name={self.first_name}\n"
            + f"last_name={self.last_name}\n"
            + f"birthday={self.birthday}\n"
            + f"created_at={self.created_at}\n"
            + ">"
        )
