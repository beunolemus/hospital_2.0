from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.usuarios_roles, config.db, schemas.usuarios_roles, models.usuarios_roles
from datetime import datetime
from typing import List
import crud.usuarios_roles, config.db, schemas.usuarios_roles, models.usuarios_roles
from config.db import SessionLocal

usuarios_roles = APIRouter()

# Dependencia para obtener la sesión de la base de datos
models.usuarios_roles.Base.metadata.create_all(bind=config.db.engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

<<<<<<< HEAD
@usuarios_roles.post("/usuarios_roles/", response_model=schemas.usuarios_roles.UsuarioRol)
def create_usuario_rol(usuario_rol: schemas.usuarios_roles.UsuarioRolCreate, db: Session = Depends(get_db)):
    db_usuario_rol = models.usuarios_roles.UsuarioRol(**usuario_rol.dict(), Fecha_Registro=datetime.now(), Fecha_Actualizacion=datetime.now())
=======
@usuario_roles.post("/usuarios_roles/", response_model=schemas.UsuarioRol)
def create_usuario_rol(usuario_rol: schemas.UsuarioRolCreate, db: Session = Depends(get_db)):
    db_usuario_rol = models.UsuarioRol(**usuario_rol.dict(), Fecha_Registro=datetime.now())
>>>>>>> c5df8eb49d425aa5ff9d25e8d8f56cf45b793b28
    db.add(db_usuario_rol)
    db.commit()
    db.refresh(db_usuario_rol)
    return db_usuario_rol

<<<<<<< HEAD
@usuarios_roles.get("/usuarios_roles/", response_model=List[schemas.usuarios_roles.UsuarioRol])
=======
@usuario_roles.get("/usuarios_roles/", response_model=List[schemas.UsuarioRol])
>>>>>>> c5df8eb49d425aa5ff9d25e8d8f56cf45b793b28
def read_usuarios_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.usuarios_roles.UsuarioRol).offset(skip).limit(limit).all()

<<<<<<< HEAD
@usuarios_roles.put("/usuarios_roles/{usuario_id}/{rol_id}", response_model=schemas.usuarios_roles.UsuarioRol)
def update_usuario_rol(usuario_id: int, rol_id: int, usuario_rol: schemas.usuarios_roles.UsuarioRolUpdate, db: Session = Depends(get_db)):
    db_usuario_rol = crud.usuarios_roles.update_usuario_rol(db=db, usuario_id=usuario_id, rol_id=rol_id, usuario_rol=usuario_rol)
    if db_usuario_rol is None:
        raise HTTPException(status_code=404, detail="UsuarioRol no encontrado")
    db_usuario_rol.Fecha_Actualizacion = datetime.now()
    return db_usuario_rol

@usuarios_roles.delete("/usuarios_roles/{usuario_id}/{rol_id}", response_model=schemas.usuarios_roles.UsuarioRol)
def delete_usuario_rol(usuario_id: int, rol_id: int, db: Session = Depends(get_db)):
    db_usuario_rol = crud.usuarios_roles.delete_usuario_rol(db=db, usuario_id=usuario_id, rol_id=rol_id)
    if db_usuario_rol is None:
        raise HTTPException(status_code=404, detail="UsuarioRol no encontrado")
    return db_usuario_rol
=======
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
>>>>>>> c5df8eb49d425aa5ff9d25e8d8f56cf45b793b28
