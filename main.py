from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, EmailStr
from fastapi.exceptions import HTTPException

class Mensaje(BaseModel):
    id: Optional[int] = None
    user: str
    message: str

app = FastAPI()

# Base de datos simulada
mensajes_db = []


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
    raise HTTPException(status_code=404, detail=", mensaje no encontrada")

@app.post("/mensajes", response_model=Mensaje)
def crear_mensaje(mensaje: Mensaje):
    mensaje.id = len(mensajes) + 1
    mensajes.append(mensaje)
    return mensaje 
    raise HTTPException(status_code=404, detail=", mensaje no encontrada")


@app.put("/mensajes/{id}", response_model=Mensaje)
def actualizar_mensaje(mensaje_id : int, mensaje: Mensaje):
    for index, mensaje in enumerate(mensajes):
        if mensaje.id == mensaje_id:
            mensajes[index].update(mensaje)
            return mensajes[index]
    return {"error": "mensaje no encontrado"}
    raise HTTPException(status_code=404, detail=", mensaje no encontrada")


@app.delete("/mensajes/{mensaje_id}", response_model=dict)
def eliminar_mensaje(persona_id: int):
    for index, mensajes in enumerate(mensajes_db):
        if mensajes.id == persona_id:
            del mensajes_db[index]
    return {"detail": "Persona eliminada"}
    raise HTTPException(status_code=404, detail=", mensaje no encontrada")



    