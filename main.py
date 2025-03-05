#Se importa Fastapi y librerias de exepciones
from fastapi import FastAPI, HTTPException, Depends, status

#se importa BaseModel para la validacion de datos 
from pydantic import BaseModel
#Se importa libreria para datos opcionales
from typing import Optional, Annotated
#se importa la clase models del proyecto
import models
#Se importa manejo de bases de datos 
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from datetime import date



#Se crea un obejto para instanciar la clase
app = FastAPI()
#Se genera una clase para la validacion de datos 
class Validacion_Datos(BaseModel):
    nombre:str
    categoria:str
    descripcion:str
    fecha:date
    provincia:str
    canton:str
    distrito:str
    url:str
    adicional: Optional[str] = None


#Se genera una clase para la validacion de datos 
class Consulta(BaseModel):
    id:int
    nombre:str
    categoria:str
    descripcion:str
    fecha:date
    provincia:str
    canton:str
    distrito:str
    url:str
    adicional: Optional[str] = None

#Se genera funcion para manejo de session de la base de datos
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]



#Se genera funcion para listar leyendas
@app.get("/listarregistros/", status_code=status.HTTP_200_OK)
async def consultar_registros(db:db_dependency):
    registros = db.query(models.registro_leyenda).all()
    return registros

#se genera la ruta y funcion para agregar leyendas a la base de datos

@app.post("/registro/", status_code=status.HTTP_201_CREATED)
async def crear_registro(registro:Validacion_Datos, db:db_dependency):
    db_registro = models.registro_leyenda(**registro.dict())
    db.add(db_registro)
    db.commit()
    return {" fue creado el registro ":db_registro }

#Se genera metodo para consultar registro por id
@app.get("/consultaregistro/{id}", status_code=status.HTTP_200_OK)
async def consultar_registros_por_documento(id_leyenda, db:db_dependency):
    registro = db.query(models.registro_leyenda).filter(models.registro_leyenda.id==id_leyenda).first()
    if registro is None:
        HTTPException(status_code=404, detail="Registro no encontrado")
    return registro


#Se genera funcion para eliminar registros segun el id
@app.delete("/borrarregisro/{id}", status_code=status.HTTP_200_OK)
async def borrar_registro(id_registro, db:db_dependency):
    registroborrar = db.query(models.registro_leyenda).filter(models.registro_leyenda.id==id_registro).first()
    if registroborrar is None:
        HTTPException(status_code=404, detail="No se puede borrar no exite el registro")
    db.delete(registroborrar)
    db.commit()
    return "EL registro de elimino exitosamente"


#Se genera funcion para actualizar registros segun el id
@app.post("/actualizarregistro/", status_code=status.HTTP_200_OK)
async def actualizar_registro (registro:Consulta, db:db_dependency):
     registroactualizar = db.query(models.registro_leyenda).filter(models.registro_leyenda.id==registro.id).first()
     if registroactualizar is None:
         HTTPException(status_code=404, detail="No se encuentra el registro")
     registroactualizar.id = registro.id
     registroactualizar.nombre = registro.nombre
     registroactualizar.categoria=registro.categoria
     registroactualizar. descripcion = registro.descripcion
     registroactualizar.fecha=registro.fecha
     registroactualizar.provincia=registro.provincia
     registroactualizar.canton=registro.canton
     registroactualizar.distrito=registro.distrito
     registroactualizar.url=registro.url
     registroactualizar.adicional=registro.adicional
     db.commit()
     return "Registro actualizado exitosamente"

