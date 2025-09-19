#Se importa Fastapi y librerias de excepciones
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

#se crean las tablas en la base de datos
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()

#Se crea un objeto para instanciar la clase
app = FastAPI(title="API de Leyendas", description="API para gestionar registros de leyendas", version="1.0.0")

#Se genera funcion para listar leyendas
@app.get("/listarregistros/", status_code=status.HTTP_200_OK)
async def consultar_registros(session: SessionDep):
    try:
        registros = session.query(Registro).all()
        return {"registros": registros, "total": len(registros)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar registros: {str(e)}")

#se genera la ruta y funcion para agregar leyendas a la base de datos
@app.post("/registro/", status_code=status.HTTP_201_CREATED)
async def crear_registro(registro: Registro, session: SessionDep):
    try:
        print("=== DEBUG: Datos recibidos ===")
        print(f"Registro: {registro}")
        print(f"Tipo de registro: {type(registro)}")
        
        session.add(registro)
        print("=== DEBUG: Registro agregado a sesión ===")
        
        session.commit()
        print("=== DEBUG: Commit exitoso ===")
        
        session.refresh(registro)
        print("=== DEBUG: Refresh exitoso ===")
        
        return {"mensaje": "Registro creado exitosamente", "registro": registro}
        
    except Exception as e:
        print(f"=== DEBUG: Error capturado ===")
        print(f"Error tipo: {type(e)}")
        print(f"Error mensaje: {str(e)}")
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear registro: {str(e)}")
    
    
#Se genera metodo para consultar registro por id
@app.get("/consultaregistro/{id_leyenda}", status_code=status.HTTP_200_OK)
async def consultar_registro_por_id(id_leyenda: int, session: SessionDep):
    try:
        registro = session.query(Registro).filter(Registro.id == id_leyenda).first()
        if registro is None:
            raise HTTPException(status_code=404, detail="Registro no encontrado")
        return registro
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar registro: {str(e)}")

#Se genera funcion para eliminar registros segun el id
@app.delete("/borrarregistro/{id_registro}", status_code=status.HTTP_200_OK)
async def borrar_registro(id_registro: int, session: SessionDep):
    try:
        registro_borrar = session.query(Registro).filter(Registro.id == id_registro).first()
        if registro_borrar is None:
            raise HTTPException(status_code=404, detail="No se puede borrar, no existe el registro")
        
        session.delete(registro_borrar)
        session.commit()
        return {"mensaje": "El registro se eliminó exitosamente"}
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Error al eliminar registro: {str(e)}")

#Se genera funcion para actualizar registros segun el id
@app.put("/actualizarregistro/{id_registro}", status_code=status.HTTP_200_OK)
async def actualizar_registro(id_registro: int, registro: Registro, session: SessionDep):
    try:
        registro_actualizar = session.query(Registro).filter(Registro.id == id_registro).first()
        if registro_actualizar is None:
            raise HTTPException(status_code=404, detail="No se encuentra el registro")
        
        # Actualizar campos
        registro_actualizar.nombre = registro.nombre
        registro_actualizar.categoria = registro.categoria
        registro_actualizar.descripcion = registro.descripcion
        registro_actualizar.fecha = registro.fecha
        registro_actualizar.provincia = registro.provincia
        registro_actualizar.canton = registro.canton
        registro_actualizar.distrito = registro.distrito
        registro_actualizar.url = registro.url
        registro_actualizar.adicional = registro.adicional
        
        session.commit()
        session.refresh(registro_actualizar)
        return {"mensaje": "Registro actualizado exitosamente", "registro": registro_actualizar}
    except HTTPException:
        raise
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar registro: {str(e)}")

# Endpoint adicional para verificar el estado de la API
@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"mensaje": "API de Leyendas funcionando correctamente", "documentacion": "/docs"}
