from sqlalchemy import Column, String, Integer
from db import Base, engine

class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(30), unique=True)
    email = Column(String(30), unique=True)

Base.metadata.create_all(engine)