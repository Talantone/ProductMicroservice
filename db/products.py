import uuid

import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .base import metadata, Base


class Product(Base):
    __tablename__ = "products"
    UUID = sqlalchemy.Column(sqlalchemy.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True)
    description = sqlalchemy.Column(sqlalchemy.String)
    offers = relationship("Offer", back_populates="product")


class Offer(Base):
    __tablename__ = "offers"
    UUID = sqlalchemy.Column(sqlalchemy.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = sqlalchemy.Column(sqlalchemy.UUID, ForeignKey(Product.UUID), nullable=False)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    items_in_stock = sqlalchemy.Column(sqlalchemy.Integer)
    product = relationship("Product", back_populates="offers")
