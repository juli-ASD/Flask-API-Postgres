from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


Base = declarative_base() #Permitir ralizar el mapeo de la base de datos
engine = create_engine("postgresql://postgres:root@localhost:5432/flask_db") #conectar a base de datos

Session = sessionmaker(bind=engine) #Guardar transacciones en base datos