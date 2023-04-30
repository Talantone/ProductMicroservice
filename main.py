from fastapi import FastAPI

app = FastAPI(title="Product microservice")


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", port=APP_PORT, host=APP_ADDR, reload=True)