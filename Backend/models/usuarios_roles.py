from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class UsuarioRol(Base):
    __tablename__ = "usuarios_roles"

    Usuario_ID = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    Rol_ID = Column(Integer, ForeignKey('roles.id'), primary_key=True)
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
    # Definición de relaciones si es necesario
    usuario = relationship("Usuario", back_populates="roles")
    rol = relationship("Rol", back_populates="usuarios")

    def __repr__(self):
        return f"<UsuarioRol(Usuario_ID={self.Usuario_ID}, Rol_ID={self.Rol_ID}, Estatus={self.Estatus}, Fecha_Registro={self.Fecha_Registro}, Fecha_Actualizacion={self.Fecha_Actualizacion})>"
