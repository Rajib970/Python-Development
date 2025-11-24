from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

""" Before Working with MySQL, dwonwload the MySQL installer (for MySQL Workbench) and setup DBMS in the system"""
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db' 

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SesionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()