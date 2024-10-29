from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Mensaje(BaseModel):
    id: Optional[int] = None
    user: str
    message: str

app = FastAPI()

mensajes = []

@app.get("/")
def listar_mensajes():
    return mensajes

@app.get("/mensajes/{id}", response_model=Mensaje)
def obtener_mensaje(id: int):
    for mensaje in mensajes:
        if mensaje["id"] == id:
            return mensaje
    return {"error": "mensaje no encontrado"}