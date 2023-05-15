import asyncio

import sqlalchemy
import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import db
from core.config import APP_PORT, APP_ADDR
from core.offer_service_requests import send_post_request_access
from core.periodical_services import access_service, offers_service
from db import engine, base
from db.base import SessionLocal
from endpoints import users, auth, products
from repository.product import get_all_ids

base.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Product microservice")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/login", tags=["login"])
app.include_router(products.router, prefix="/products", tags=["products"])


@app.on_event("startup")
async def startup():
    asyncio.create_task(access_service())
    asyncio.create_task(offers_service(product_ids=await get_all_ids(db=SessionLocal()), db=SessionLocal()))



if __name__ == '__main__':
    uvicorn.run("main:app", port=APP_PORT, host=APP_ADDR, reload=True)

