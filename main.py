from fastapi import FastAPI
from pydantic import BaseModel
from typing import List  # Asegurar que se importe List

app = FastAPI()

# Lista de usuarios en memoria
users = []

# Modelo de usuario
class User(BaseModel):
    id: int
    name: str
    email: str

# Endpoint POST para agregar usuarios
@app.post("/users/")
async def add_user(user: User):
    users.append(user)
    return {"message": "Usuario agregado correctamente", "user": user}

# Endpoint GET para obtener usuarios
@app.get("/users/", response_model=List[User])
async def get_users():
    return users

