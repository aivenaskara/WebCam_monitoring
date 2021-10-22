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

    def __repr__(self):
        return f'<Фотография {self.id} сделана {self.created_on}>'


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(120), unique=True)

    def __repr__(self):
        return f'<User {self.name} {self.email}>'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
