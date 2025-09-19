import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Cambiar a SQLite (no necesita servidor)
URL_DATABASE = 'sqlite:///./leyendas.db'
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

try:
    engine = create_engine(URL_DATABASE, echo=True)  # echo=True para debug
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    print("✅ Conexión a la base de datos establecida correctamente")
except Exception as e:
    print(f"❌ Error al conectar con la base de datos: {e}")
    raise