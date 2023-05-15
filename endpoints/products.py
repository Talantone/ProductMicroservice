from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.offer_service_requests import send_post_request_register_product
from core.utils import get_access
from db.base import get_db
from db.base import SessionLocal
from endpoints.depends import get_current_user
from models.user import User
from repository.offer import get_all_product_offers
from repository.product import get_all, get_by_id, create, update, delete, get_all_ids
from models.product import ProductSchema, ProductInSchema, OfferSchema, OfferOutSchema

router = APIRouter()


@router.get("/", response_model=List[ProductSchema])
async def get_all_products(db: Session = Depends(get_db),
                           current_user: User = Depends(get_current_user),
                           limit: int = 100,
                           skip: int = 0):
    return await get_all(db=db, limit=limit, skip=skip)


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product_by_id(product_id: str,
                            db: Session = Depends(get_db),
                            current_user: User = Depends(get_current_user)):
    return await get_by_id(db=db, product_id=product_id)


@router.get("/{product_id}/offers/", response_model=List[OfferOutSchema])
async def get_product_offers(product_id: str,
                             db: Session = Depends(get_db),
                             current_user: User = Depends(get_current_user)):
    return await get_all_product_offers(product_id=product_id, db=db)


@router.post("/", response_model=ProductSchema)
async def create_product(p: ProductInSchema,
                         db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    res = await create(db=db, p=p)
    access = await get_access()
    response_from_service = await send_post_request_register_product(product=res, access=access)
    print(response_from_service)
    return res


@router.put("/", response_model=ProductSchema)
async def update_product(p: ProductInSchema,
                         product_id: str,
                         db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    return await update(db=db, p=p, product_id=product_id)


@router.delete("/")
async def delete_product(product_id: str,
                         db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    return await delete(db=db, product_id=product_id)


@router.get("/product_ids")
async def get_all_products_ids(db: Session = Depends(get_db),
                               current_user: User = Depends(get_current_user)):
    return await get_all_ids(db=db)
