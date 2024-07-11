from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UsuarioRolBase(BaseModel):
    Usuario_ID: int
    Rol_ID: int
    Estatus: Optional[bool] = None

class UsuarioRolCreate(UsuarioRolBase):
    pass

class UsuarioRolUpdate(UsuarioRolBase):
    pass

class UsuarioRol(UsuarioRolBase):
    Fecha_Registro: Optional[datetime]
    Fecha_Actualizacion: Optional[datetime]

    class Config:
        orm_mode = True
