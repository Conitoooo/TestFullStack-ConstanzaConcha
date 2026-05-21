from pydantic import BaseModel
from typing import Optional

class TiendaInfo(BaseModel):
    codigo: str
    nombre: str
    tipo: str

class StationData(BaseModel):
    id: str
    compania: str
    direccion: str
    comuna: str
    region: str
    latitud: float
    longitud: float
    distancia_lineal: float 
    precio_solicitado: int 
    tienda: Optional[TiendaInfo] = None
    tiene_tienda: bool

class SearchResponse(BaseModel):
    success: bool
    data: StationData