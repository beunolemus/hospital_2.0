# models/usuarios.py
from sqlalchemy import Column, Integer, String
from config.db import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

# models/roles.py
from sqlalchemy import Column, Integer, String
from config.db import Base

class Rol(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

# models/usuarios_roles.py
from sqlalchemy import Column, ForeignKey, Integer
from config.db import Base
from models.usuarios import Usuario
from models.roles import Rol

class UsuarioRol(Base):
    __tablename__ = 'usuarios_roles'
    id = Column(Integer, primary_key=True, index=True)
    Usuario_ID = Column(Integer, ForeignKey('usuarios.id'))
    Rol_ID = Column(Integer, ForeignKey('roles.id'))
