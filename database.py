#Se importan las librerias para el manejo de la base de datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Se crea la conexion a la base de datos
URL_DATABASE = "mysql+pymysql://root:@localhost:3307/4thewords_prueba_wendy_cardenas"
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()