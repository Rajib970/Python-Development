from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

""" Before Working with PostgreSQl, dwonwload the Postgrsql installer and setup DBMS in the system"""
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:rajib@localhost/TodoApplicationDB' 

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SesionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()