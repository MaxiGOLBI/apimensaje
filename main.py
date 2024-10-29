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

@app.post("/mensajes", response_model=Mensaje)
def crear_mensaje(mensaje: Mensaje):
    mensaje.id = len(mensajes) + 1
    mensajes.append(mensaje)
    return mensaje 

app.put("/mensajes/{id}", response_model=Mensaje)
def actualizar_mensaje(mensaje_id : int, mensaje: Mensaje):
    for index, mensaje in enumerate(mensajes):
        if mensaje.id == mensaje_id:
            mensajes[index].update(mensaje)
            return mensajes[index]
    return {"error": "mensaje no encontrado"}


    