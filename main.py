import uvicorn
from fastapi import FastAPI

import db
from core.config import APP_PORT, APP_ADDR
from db import engine, base
from endpoints import users, auth, products

base.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Product microservice")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/login", tags=["login"])
app.include_router(products.router, prefix="/products", tags=["products"])
#@app.on_event("startup")
#async def startup():
    #await database.connect()

#@app.on_event("shutdown")
#async def shutdown():
   #await database.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", port=APP_PORT, host=APP_ADDR, reload=True)
