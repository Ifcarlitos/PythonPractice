from fastapi import FastAPI

from .db import Base, engine
from .api import auth, courses

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PyLearn API")

app.include_router(auth.router)
app.include_router(courses.router)

@app.get("/")
async def root():
    return {"message": "Welcome to PyLearn API"}
