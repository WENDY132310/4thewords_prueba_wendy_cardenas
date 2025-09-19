from sqlalchemy import Integer, Column,Date,Text,String
from database import Base
from sqlmodel import Field, SQLModel
from datetime import date       


#Se crea clase para el manejo de registros de la base de datos con su respectiva estructura
# #class registro_leyenda(Base):
#         __tablename__="registro_leyenda"
#         id=Column(Integer, primary_key=True, index=True)
#         nombre=Column(String(200))
#         categoria=Column(String(100))
#         descripcion=Column(Text)
#         fecha=Column(Date)
#         provincia=Column(String(100))
#         canton=Column(String(100))
#         distrito=Column(String(100))
#         url=Column(String(500))
#         adicional=Column(String(1000))

class Registro(SQLModel, table=True):
    __tablename__ = "registro_leyenda"
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    categoria: str
    descripcion: str
    fecha: str
    provincia: str
    canton: str
    distrito: str
    url: str
    adicional:str 
    