# Api de búsqueda de estaciones de combustible
## Esta es una API Rest desarrollada por Constanza Concha con FastApi

### Requisitos:
-Python desde v3.8
-Entorno Virtual

### Instalacion:
-Clonar repositorio:
    git clone 

### Activar entorno virtual:
   *En Windows:
     venv\Scripts\activate
     pip install -r requirements.txt     
   *En mac/Linux:
     source venv/bin/activate
     pip install -r requirements.txt

### Iniciar el servidor:
   uvicorn app.main:app --reload

### Cuando esté corriendo el servidor, ingrese esto en el navegador:
http://127.0.0.1:8000/api/stations/search?lat={latitud}&lng={longitud}&product={producto}&nearest=true&store=true&cheapest=true
(tiene que reemplazar "{latitud}", "{longitud}" y "{producto}" con la información que quiera usar)

### Si lo desea, FastAPI genera automáticamente una interfaz gráfica... 
Les solicito ingresar desde su navegador a: http://127.0.0.1:8000/docs