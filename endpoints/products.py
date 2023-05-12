from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.base import get_db
from db.base import SessionLocal
from repository.product import get_all, get_by_id, create, update, delete
from models.product import ProductSchema, ProductInSchema, OfferSchema

router = APIRouter()


@router.get("/", response_model=List[ProductSchema])
async def get_all_products(db: Session = Depends(get_db),
                           limit: int = 100,
                           skip: int = 0):
    return await get_all(db=db, limit=limit, skip=skip)


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product_by_id(product_id: str,
                            db: Session = Depends(get_db)):
    return await get_by_id(db=db, product_id=product_id)


@router.post("/", response_model=ProductSchema)
async def create_product(p: ProductInSchema,
                         db: Session = Depends(get_db)):
    return await create(db=db, p=p)


@router.put("/", response_model=ProductSchema)
async def update_product(p: ProductInSchema,
                         product_id: str,
                         db: Session = Depends(get_db)):
    return await update(db=db, p=p, product_id=product_id)


@router.delete("/")
async def delete_product(product_id: str,
                         db: Session = Depends(get_db)):
    return await delete(db=db, product_id=product_id)
