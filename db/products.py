import sqlalchemy
from base import metadata

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("UUID", sqlalchemy.UUID, primary_key=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column("description", sqlalchemy.String)
)

offers = sqlalchemy.Table(
    "offers",
    metadata,
    sqlalchemy.Column("UUID", sqlalchemy.UUID, primary_key=True, unique=True),
    sqlalchemy.Column("product_id", sqlalchemy.UUID, sqlalchemy.ForeignKey(products.UUID), nullable=False),
    sqlalchemy.Column("price", sqlalchemy.Integer),
    sqlalchemy.Column("items_in_stock", sqlalchemy.Integer)
)
