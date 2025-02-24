from fastapi import FastAPI #add_users
from pydantic import BaseModel #add_users

from typing import List #get_users

#add_users

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/")
async def add_user(user: User):
    users.append(user)
    return {"message": "Usuario agregado correctamente", "user": user}

#get_users

@app.get("/users/", response_model=List[User])
async def get_users():
    return users
