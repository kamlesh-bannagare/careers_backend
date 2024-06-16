from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine
from app.models import item, user
from app.api.v1.endpoints import items, users

app = FastAPI()

item.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

app.include_router(items.router, prefix=f"{settings.API_V1_STR}/items", tags=["items"])
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)