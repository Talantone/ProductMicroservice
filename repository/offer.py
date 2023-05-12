from typing import Optional, List

import sqlalchemy
from sqlalchemy.orm import Session

from db.products import Offer, Product
from models.product import OfferSchema


async def create_all(db: Session, product_id: str, offer_list: List[OfferSchema]) -> List[OfferSchema]:
    product = db.query(Product).filter(Product.UUID == product_id).first()
    if product is not None:
        for offer in offer_list:
            offer.product_id = product_id
    db.add_all(offer_list)
    db.commit()
    db.refresh(offer_list)
    db.execute(sqlalchemy.update(Product).where(Product.id == product_id).values(offers=offer_list))
    return offer_list


async def delete_all(db: Session, product_id: str):
    product = db.query(Product).filter(Product.UUID == product_id).first()
    offers_to_delete = db.query(Offer).filter(Offer.product.UUID == product_id)
    db.delete(offers_to_delete)
    db.delete(product.offers)
    db.commit()
