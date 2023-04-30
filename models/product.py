from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: Optional[str] = None
    name: str
    description: str


class Offer(BaseModel):
    id: Optional[str] = None
    product_id: str
    name: str
    items_in_stock: int


class ProductIn(BaseModel):
    name: str
    description: str
