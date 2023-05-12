from .products import Product, Offer
from .users import User
from .base import metadata, engine

metadata.create_all(bind=engine)