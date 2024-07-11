from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class UsuarioRolBase(BaseModel):
    Usuario_ID: int
    Rol_ID: int
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UsuarioRolCreate(UsuarioRolBase):
    pass

class UsuarioRolUpdate(UsuarioRolBase):
    pass

class UsuarioRol(UsuarioRolBase):
    class Config:
        orm_mode = True
