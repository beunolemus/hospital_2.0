from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(255))
    password = Column(LONGTEXT)
    created_at = Column(DateTime)
    estatus = Column(Boolean, default=False)
    Id_persona = Column(Integer)
<<<<<<< HEAD
    #items = relationship("Item", back_populates="owner") Clave Foranea
=======

    # items = relationship("Item", back_populates="owner")  # Clave Foránea
>>>>>>> 18a0686ba9476220cf5ad14205bf2efe0c4c7c3c
