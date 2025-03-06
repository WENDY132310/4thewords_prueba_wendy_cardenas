#Se importa Fastapi y librerias de exepciones
from fastapi import FastAPI, HTTPException, Depends, status
#se importa BaseModel para la validacion de datos 
from pydantic import BaseModel
#Se importa libreria para datos opcionales
from typing import Optional, Annotated
#se importa la clase models del proyecto
from models import Registro
#Se importa manejo de bases de datos 
from database import engine, SessionLocal
from sqlmodel import Field, SQLModel, Session
from datetime import date
from contextlib import asynccontextmanager

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


#se crean las tabla en la base de datos
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()

#Se crea un objeto para instanciar la clase
app = FastAPI()

#Se genera funcion para listar leyendas
@app.get("/listarregistros/", status_code=status.HTTP_200_OK)
async def consultar_registros(session: SessionDep):
    registros = session.query(Registro).all()
    return registros

#se genera la ruta y funcion para agregar leyendas a la base de datos

@app.post("/registro/")
async def crear_registro(registro:Registro, session: SessionDep):
    session.add(registro)
    session.commit()
    session.refresh(registro)
    return {" fue creado el registro ":registro }
    

#Se genera metodo para consultar registro por id
@app.get("/consultaregistro/{id}", status_code=status.HTTP_200_OK)
async def consultar_registros_por_documento(id_leyenda, session: SessionDep):
    registro = session.query(Registro).filter(Registro.id==id_leyenda).first()
    if registro is None:
        HTTPException(status_code=404, detail="Registro no encontrado")
    return registro


#Se genera funcion para eliminar registros segun el id
@app.delete("/borrarregisro/{id}", status_code=status.HTTP_200_OK)
async def borrar_registro(id_registro, session: SessionDep):
    registroborrar = session.query(Registro).filter(Registro.id==id_registro).first()
    if registroborrar is None:
        HTTPException(status_code=404, detail="No se puede borrar no exite el registro")
    session.delete(registroborrar)
    session.commit()
    return "EL registro de elimino exitosamente"


#Se genera funcion para actualizar registros segun el id
@app.post("/actualizarregistro/", status_code=status.HTTP_200_OK)
async def actualizar_registro(registro: Registro, session: SessionDep):
    registroactualizar = session.query(Registro).filter(Registro.id == registro.id).first()
    if registroactualizar is None:
        raise HTTPException(status_code=404, detail="No se encuentra el registro")
    registroactualizar.id = registro.id
    registroactualizar.nombre = registro.nombre
    registroactualizar.categoria = registro.categoria
    registroactualizar.descripcion = registro.descripcion
    registroactualizar.fecha = registro.fecha
    registroactualizar.provincia = registro.provincia
    registroactualizar.canton = registro.canton
    registroactualizar.distrito = registro.distrito
    registroactualizar.url = registro.url
    registroactualizar.adicional = registro.adicional
    session.commit()
    return "Registro actualizado exitosamente"

