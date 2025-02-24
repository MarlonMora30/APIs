from fastapi import FastAPI
from pydantic import BaseModel

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
