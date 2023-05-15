from typing import Optional, List

import sqlalchemy
from sqlalchemy.orm import Session

from core.utils import parse_uuid
from db.products import Offer, Product
from models.product import OfferSchema
from .product import get_by_id


async def create_all(db: Session, product_id: str, offer_list: List[OfferSchema]) -> List[OfferSchema]:
    product = db.query(Product).filter(Product.UUID == product_id).first()
    offers_db = []
    if product is not None:
        for offer in offer_list:
            offers_db.append(Offer(
                id=offer.id,
                product_id=product_id,
                price=offer.price,
                items_in_stock=offer.items_in_stock,
                product=product
            ))
    db.add_all(offers_db)
    db.commit()
    # db.refresh(offers_db)
    # db.execute(sqlalchemy.update(Product).where(Product.id == product_id).values(offers=offers_db))
    # db.commit()
    return offers_db


async def get_all_product_offers(db: Session, product_id: str):
    product = db.query(Product).filter(Product.UUID == product_id).first()
    offers = []
    for offer in product.offers:
        offer.product_id = str(offer.product_id)
        offers.append(offer)
    return offers


async def delete_all(db: Session, product_id: str):
    product = db.query(Product).filter(Product.UUID == product_id).first()

    db.execute(sqlalchemy.delete(Offer).where(Offer.product_id == product_id))
    db.commit()
