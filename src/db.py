from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

Base = declarative_base()
engine = create_engine("postgresql://postgres:root@localhost:5432/flask_db")

Session = sessionmaker(bind=engine)