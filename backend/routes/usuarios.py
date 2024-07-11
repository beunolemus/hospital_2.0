from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

usuario = APIRouter()
usuarios = []

class ModelUsuarios(BaseModel):
    id: int
    usuario: str
    primer_apellido: str
    contrasena: str
    id_persona: str
    estatus: bool = False
    creacion_at: datetime = datetime.now()

@usuario.get("/")
def bienvenida():
    return "Bienvenido al API"

@usuario.get("/usuarios")
def get_personas():
    return usuarios

@usuario.post("/usuarios")
def save_personas(datos_usuarios: ModelUsuarios):
    usuarios.append(datos_usuarios)
    return "Datos Guardados Correctamente"


def get_usuarios(usuario_id: int):
    for usuario in usuario:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="usuario no encontrada")



@usuario.put("/usuarios/{usuario_id}")
def update_usuario(usuario_id: int, datos_usuarios: ModelUsuarios):
    for index, usuario in enumerate(usuarios ):
        if usuario.id == usuario_id:
            usuarios[index] = datos_usuarios
            return "Datos Actualizados Correctamente"
    raise HTTPException(status_code=404, detail="Usuario no encontrada")

@usuario.delete("/usuarios/{usuario_id}")
def delete_usuario(usuario_id: int):
    for index, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios.pop(index)
            return "Datos Eliminados Correctamente"
    raise HTTPException(status_code=404, detail="Usuario no encontrada")