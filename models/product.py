import uuid
from typing import Optional
from pydantic import BaseModel


class ProductSchema(BaseModel):
    UUID: Optional[str] | Optional[uuid.UUID]
    name: str
    description: str

    class Config:
        orm_mode = True


class OfferSchema(BaseModel):
    id: Optional[str] | Optional[uuid.UUID]
    product_id: str
    price: int
    items_in_stock: int

    class Config:
        orm_mode = True


class OfferOutSchema(BaseModel):
    id: Optional[str] | Optional[uuid.UUID]
    price: int
    items_in_stock: int

    class Config:
        orm_mode = True


class ProductInSchema(BaseModel):
    name: str
    description: str
