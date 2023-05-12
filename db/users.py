import sqlalchemy
from .base import metadata, Base


class User(Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True)
    email = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
