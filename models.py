from datetime import datetime

from sqlalchemy.sql.sqltypes import Boolean
from db import Base, engine
from sqlalchemy import Column, Integer, String, DateTime, BLOB


class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    camera_name = Column(String)
    photo = Column(BLOB)
    created_on = Column(DateTime(), default=datetime.now)
    detect = Column(Boolean)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(128))
    role = Column(String(10))
    email = Column(String(120), unique=True)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
