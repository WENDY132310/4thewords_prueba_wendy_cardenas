# Proyecto 4thewords_prueba

Este proyecto es una API para gestionar registros de leyendas utilizando FastAPI y Sqlmoldel con una base de datos MySQL.

## Requisitos
Los requisitos y tecnologias usados para el funcionamiento del programa estan relacionados por nombre y version en el archivo "requeriments.txt"


## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd 4thewords_prueba
    ```
2. Crea un entorno virtual e instálalo:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # En Windows
    ```
3. Instala las dependencias relacionadas previamente :
    ```sh
    pip install -r requirements.txt
    ```
4. Configura la base de datos:
    - Asegúrate de que MySQL esté en ejecución.
    - Crea la base de datos `4thewords_prueba_wendy_cardenas`:
    ```sql
    CREATE DATABASE leyendasbd;
5. Crea las tablas en la base de datos:

    ```sql
   CREATE TABLE `registro_leyenda` (
  `id` int AUTO_INCREMENT PRIMARY KEY,
  `nombre` varchar(200) COLLATE utf32_spanish2_ci NOT NULL,
  `categoria` varchar(100) CHARACTER SET utf32 COLLATE utf32_spanish2_ci NOT NULL,
  `descripcion` text COLLATE utf32_spanish2_ci NOT NULL,
  `fecha` date NOT NULL,
  `provincia` varchar(100) COLLATE utf32_spanish2_ci NOT NULL,
  `canton` varchar(100) COLLATE utf32_spanish2_ci NOT NULL,
  `distrito` varchar(100) COLLATE utf32_spanish2_ci NOT NULL,
  `url` varchar(500) COLLATE utf32_spanish2_ci NOT NULL,
  `adicional` varchar(1000) COLLATE utf32_spanish2_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_spanish2_ci;

INSERT INTO registro_leyenda (nombre, categoria, descripcion, fecha, provincia, canton, distrito, url, adicional) VALUES
('El Pirata Cofresí', 'Piratas y Tesoros', 'Roberto Cofresí, un pirata puertorriqueño que robaba a los ricos para dar a los pobres.', '1825-03-29', 'San Germán', 'San Germán', 'San Germán Pueblo', 'https://ejemplo.com/cofresi.jpg', 'Se dice que escondió muchos tesoros en la isla.'),
('La Garita del Diablo', 'Lugares Embrujados', 'Una garita en el Castillo San Felipe del Morro donde se escuchan ruidos extraños y se ven sombras.', '1700-01-01', 'San Juan', 'San Juan Antiguo', 'Ballajá', 'https://ejemplo.com/garita.jpg', 'Se cree que un soldado murió allí y su alma vaga por la garita.'),
('La Piedra Escrita de Jayuya', 'Petroglifos', 'Un gran petroglifo con símbolos taínos que representan la cultura y creencias de los indígenas.', '1500-01-01', 'Jayuya', 'Jayuya', 'Jayuya Pueblo', 'https://ejemplo.com/piedra_escrita.jpg', 'Es uno de los petroglifos más grandes y importantes de Puerto Rico.'),
('El Chupacabras', 'Criaturas Míticas', 'Una criatura que ataca al ganado y les chupa la sangre.', '1995-03-01', 'Canóvanas', 'Canóvanas', 'Canóvanas Pueblo', 'https://ejemplo.com/chupacabras.jpg', 'Se han reportado avistamientos en toda la isla y en otros países.'),
('La Cueva del Indio', 'Cuevas y Petroglifos', 'Una cueva con petroglifos taínos y una vista espectacular del mar.', '1500-01-01', 'Arecibo', 'Arecibo', 'Islote', 'https://ejemplo.com/cueva_indio.jpg', 'Es un lugar sagrado para los taínos.'),
('La Guarida del Sol', 'Lugares Míticos', 'Una cueva donde se dice que el sol se esconde por la noche.', '1500-01-01', 'Rincón', 'Rincón', 'Pueblo', 'https://ejemplo.com/guarida_sol.jpg', 'Es un lugar con mucha energía y misticismo.'),
('El Puente de los Perros', 'Puentes y Fantasmas', 'Un puente donde se escuchan ladridos de perros y se ven sombras de perros.', '1900-01-01', 'Guayama', 'Guayama', 'Guayama Pueblo', 'https://ejemplo.com/puente_perros.jpg', 'Se dice que los perros eran sacrificados allí en rituales antiguos.'),
('La Virgen de la Roca', 'Apariciones Marianas', 'Una aparición de la Virgen María en una roca en la playa.', '1953-01-01', 'Aguadilla', 'Aguadilla', 'Aguadilla Pueblo', 'https://ejemplo.com/virgen_roca.jpg', 'Es un lugar de peregrinación y devoción.'),
('El Cemí de Algodón', 'Artefactos Taínos', 'Un cemí (ídolo taíno) hecho de algodón que se encontró en una cueva.', '1500-01-01', 'Vieques', 'Vieques', 'Isabel Segunda', 'https://ejemplo.com/cemi_algodon.jpg', 'Es una pieza única y valiosa de la cultura taína.'),
('El Árbol de la Ceiba de Ponce', 'Árboles Sagrados', 'Un árbol de ceiba gigante que se considera sagrado y protector.', '1800-01-01', 'Ponce', 'Ponce', 'Ponce Pueblo', 'https://ejemplo.com/ceiba_ponce.jpg', 'Se dice que tiene poderes mágicos y que protege a la ciudad.');
    ```

## Uso de la aplicacion

1. Inicia el servidor FastAPI:

    ```sh
    uvicorn main:app --reload
    ```
2. Accede a la documentación interactiva de la API en:
    ```
    http://127.0.0.1:8000/docs
    ```

## Estructura del Proyecto

- `main.py`: Archivo principal que contiene las rutas y lógica de la API.
- `models.py`: Definición de los modelos de la base de datos utilizando SQLAlchemy.
- `database.py`: Configuración de la conexión a la base de datos.
-



### Listar registros

- **URL**: `/listarregistros/`
- **Método**: `GET`
- **Descripción**: Lista todos los registros de leyendas.

### Crear registro

- **URL**: `/registro/`
- **Método**: `POST`
- **Descripción**: Crea un nuevo registro de leyenda.
- **Body**:
    ```json
    {
        "nombre": "string",
        "categoria": "string",
        "descripcion": "string",
        "fecha": "YYYY-MM-DD",
        "provincia": "string",
        "canton": "string",
        "distrito": "string",
        "url": "string",
        "adicional": "string"
    }
    ```

### Consultar registro por ID

- **URL**: `/consultaregistro/{id}`
- **Método**: `GET`
- **Descripción**: Consulta un registro de leyenda por su ID.

### Borrar registro

- **URL**: `/borrarregistro/{id}`
- **Método**: `DELETE`
- **Descripción**: Borra un registro de leyenda por su ID.

### Actualizar registro

- **URL**: `/actualizarregistro/{id}`
- **Método**: `PUT`
- **Descripción**: Actualiza un registro de leyenda por su ID.
- **Body**:
    ```json
    {
        "nombre": "string",
        "categoria": "string",
        "descripcion": "string",
        "fecha": "YYYY-MM-DD",
        "provincia": "string",
        "canton": "string",
        "distrito": "string",
        "url": "string",
        "adicional": "string"
    }
    ```

    
