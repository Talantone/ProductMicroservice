import uuid
from typing import Optional
from pydantic import BaseModel


class ProductSchema(BaseModel):
    UUID: Optional[uuid.UUID]
    name: str
    description: str

    class Config:
        orm_mode = True


class OfferSchema(BaseModel):
    UUID: Optional[str] = None
    product_id: str
    name: str
    items_in_stock: int

    class Config:
        orm_mode = True


class ProductInSchema(BaseModel):
    name: str
    description: str
