# En el archivo routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
import crud.usuarios_roles, config.db, schemas.usuarios_roles, models.usuarios_roles
from config.db import SessionLocal

usuario_roles = APIRouter()

# Dependencia para obtener la sesión de la base de datos
models.persons.Base.metadata.create_all(bind=config.db.engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@usuario_roles.post("/usuarios_roles/", response_model=schemas.UsuarioRol)
def create_usuario_rol(usuario_rol: schemas.UsuarioRolCreate, db: Session = Depends(get_db)):
    db_usuario_rol = models.UsuarioRol(**usuario_rol.dict(), Fecha_Registro=datetime.now())
    db.add(db_usuario_rol)
    db.commit()
    db.refresh(db_usuario_rol)
    return db_usuario_rol

@usuario_roles.get("/usuarios_roles/", response_model=List[schemas.UsuarioRol])
def read_usuarios_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.UsuarioRol).offset(skip).limit(limit).all()

@usuario_roles.put("/usuarios_roles/{usuario_rol_id}", response_model=schemas.UsuarioRol)
def update_usuario_rol(usuario_rol_id: int, usuario_rol: schemas.UsuarioRolUpdate, db: Session = Depends(get_db)):
    db_usuario_rol = db.query(models.UsuarioRol).filter(models.UsuarioRol.Usuario_ID == usuario_rol_id).first()
    if db_usuario_rol:
        for var, value in vars(usuario_rol).items():
            setattr(db_usuario_rol, var, value) if value else None
        db_usuario_rol.Fecha_Actualizacion = datetime.now()
        db.commit()
        db.refresh(db_usuario_rol)
        return db_usuario_rol
    raise HTTPException(status_code=404, detail=f"UsuarioRol with id {usuario_rol_id} not found")

@usuario_roles.delete("/usuarios_roles/{usuario_rol_id}", response_model=schemas.UsuarioRol)
def delete_usuario_rol(usuario_rol_id: int, db: Session = Depends(get_db)):
    db_usuario_rol = db.query(models.UsuarioRol).filter(models.UsuarioRol.Usuario_ID == usuario_rol_id).first()
    if db_usuario_rol:
        db.delete(db_usuario_rol)
        db.commit()
        return db_usuario_rol
    raise HTTPException(status_code=404, detail=f"UsuarioRol with id {usuario_rol_id} not found")
