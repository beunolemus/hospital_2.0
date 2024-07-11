import models.usuarios_roles
import schemas.usuarios_roles
from sqlalchemy.orm import Session
import models, schemas

def get_usuario_rol(db: Session, usuario_id: int, rol_id: int):
    return db.query(models.usuarios_roles.UsuarioRol).filter(
        models.usuarios_roles.UsuarioRol.Usuario_ID == usuario_id,
        models.usuarios_roles.UsuarioRol.Rol_ID == rol_id
    ).first()

def get_usuarios_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.usuarios_roles.UsuarioRol).offset(skip).limit(limit).all()

def create_usuario_rol(db: Session, usuario_rol: schemas.usuarios_roles.UsuarioRolCreate):
    db_usuario_rol = models.usuarios_roles.UsuarioRol(**usuario_rol.dict())
    db.add(db_usuario_rol)
    db.commit()
    db.refresh(db_usuario_rol)
    return db_usuario_rol

def update_usuario_rol(db: Session, usuario_id: int, rol_id: int, usuario_rol: schemas.usuarios_roles.UsuarioRolUpdate):
    db_usuario_rol = get_usuario_rol(db, usuario_id, rol_id)
    if db_usuario_rol:
        for var, value in vars(usuario_rol).items():
            setattr(db_usuario_rol, var, value) if value else None
        db.commit()
        db.refresh(db_usuario_rol)
    return db_usuario_rol

def delete_usuario_rol(db: Session, usuario_id: int, rol_id: int):
    db_usuario_rol = get_usuario_rol(db, usuario_id, rol_id)
    if db_usuario_rol:
        db.delete(db_usuario_rol)
        db.commit()
    return db_usuario_rol
