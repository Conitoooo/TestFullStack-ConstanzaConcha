# Api de búsqueda de estaciones de combustible

Esta es una API Rest desarrollada por Constanza Concha con FastApi

Requisitos:
-Python desde v3.8
-Entorno Virtual

Instalacion:
-Clonar repositorio:
    git clone 

Activar entorno virtual:
   En Windows:
     (terminal)
     venv\Scripts\activate
     pip install -r requirements.txt
     
   En macOS/Linux:
     source venv/bin/activate
     pip install -r requirements.txt

Iniciar el servidor:
   uvicorn app.main:app --reload

Como último paso, FastAPI genera automáticamente una interfaz gráfica... 
Les solicito ingresar desde su navegador a: http://127.0.0.1:8000/docs