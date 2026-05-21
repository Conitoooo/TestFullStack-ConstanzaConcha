from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from app.services.buscadorService import procesarBusqueda

app = FastAPI(title="API Bencina en Línea", description="Prueba Técnica Constanza Concha - Búsqueda de Estaciones")

@app.get("/api/stations/search")
async def buscar_estaciones(
    lat: float = Query(..., description="Latitud de origen"),
    lng: float = Query(..., description="Longitud de origen"),
    product: str = Query(..., description="Tipo de combustible (93, 95, 97, diesel, kerosene)"),
    nearest: bool = Query(False, description="Buscar la más cercana"),
    store: bool = Query(False, description="Con tienda"),
    cheapest: bool = Query(False, description="Con menor precio")
):
    productosValidos = ["93", "95", "97", "diesel", "kerosene"]
    if product.lower() not in productosValidos:
        raise HTTPException(
            status_code=400, 
            detail="Producto inválido."
        )

    resultado = await procesarBusqueda(
        lat=lat, 
        lng=lng, 
        producto=product, 
        nearest=nearest, 
        store=store, 
        cheapest=cheapest
    )

    if not resultado:
        return JSONResponse(
            status_code=404,
            content={
                "success": False, 
                "message": "No se encontraron estaciones que coincidan con tus criterios."
            }
        )

    estacion = resultado["data_original"]
    
    tiendaDict = None
    if resultado["tiene_tienda"]:
        t_data = resultado["tienda_info"]
        tiendaDict = {
            "codigo": t_data.get("CodigoTienda", ""),
            "nombre": t_data.get("NombreTienda", ""),
            "tipo": t_data.get("Tipo", "")
        }

    llavePrecio = f"precios{product.lower()}"

    response = {
        "success": True,
        "data": {
            "id": estacion.get("CodEs", ""),
            "compania": estacion.get("Compania", ""),
            "direccion": estacion.get("Direccion", ""),
            "comuna": estacion.get("Comuna", ""),
            "region": estacion.get("Region", ""),
            "latitud": float(estacion.get("Latitud", 0)),
            "longitud": float(estacion.get("Longitud", 0)),
            "distancia(lineal)": resultado["distancia"],
            llavePrecio: resultado["precio"],
            "tienda": tiendaDict,
            "tiene_tienda": resultado["tiene_tienda"]
        }
    }

    return response