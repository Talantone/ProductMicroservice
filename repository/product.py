import uuid
from typing import List, Optional

import sqlalchemy
from fastapi import Depends
from sqlalchemy.orm import Session

from db.base import get_db
from models.product import ProductSchema, ProductInSchema
from db.products import Product


async def create(db: Session, p: ProductInSchema) -> ProductSchema:
    product = Product(
        name=p.name,
        description=p.description
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return ProductSchema(UUID=str(product.UUID), name=product.name, description=product.description)


async def update(db: Session, product_id: str, p: ProductInSchema) -> ProductSchema:
    product = ProductSchema(
        UUID=product_id,
        name=p.name,
        description=p.description,
    )
    values = {**product.dict()}

    db.execute(sqlalchemy.update(Product).where(Product.UUID == uuid.UUID(product_id)).values(**values))
    db.commit()
    return product


async def get_all(db: Session, limit: int = 100, skip: int = 0):
    return db.query(Product).offset(skip).limit(limit).all()


async def get_all_ids(db: Session = Depends(get_db)):
    return db.query(Product.UUID).all()


async def delete(db: Session, product_id: str):
    product = db.query(Product).filter(Product.UUID == uuid.UUID(product_id)).first()
    db.delete(product)
    db.commit()


async def get_by_id(db: Session, product_id: str) -> Optional[ProductSchema]:
    product = db.query(Product).filter(Product.UUID == uuid.UUID(product_id)).first()
    return ProductSchema(UUID=str(product.UUID), name=product.name, description=product.description)
