from app.services.bencinaService import obtenerEstaciones
from app.utils.localizacion import calcularDistancia
import json

mapProductos={"93":"gasolina 93", "95":"gasolina 95", "97": "gasolina 97", "diesel": "petroleo diesel", "kerosene":"Kerosene"}

async def procesarBusqueda(lat: float, lng: float, producto: str, nearest: bool=False,store:bool=False, cheapest:bool=False):
    estacionesCrudas = await obtenerEstaciones()
    print(f"Estaciones recibidas de la API: {len(estacionesCrudas) if isinstance(estacionesCrudas, list) else estacionesCrudas}")
    if isinstance(estacionesCrudas, dict):
        estacionesCrudas = estacionesCrudas.get("data", [])
        
    if not isinstance(estacionesCrudas, list):
        print(f"Error: La Api no devolvió una lista válida. Respuesta: {estacionesCrudas}")
        return None
    

    nombreProductoApi = mapProductos.get(producto.lower())
    if not nombreProductoApi:
        return None 
        
    estacionesFiltradas = []

    for estacion in estacionesCrudas:
        precioProducto = None
        combustibles = estacion.get("combustibles", [])
        for comb in combustibles:
            nombre_largo = str(comb.get("nombre_largo", "")).lower()
            
            if nombreProductoApi in nombre_largo:
                precio_raw = comb.get("precio")
                if precio_raw:
                    precioProducto = int(float(precio_raw))
                break

        if not precioProducto:
            continue

        try:
            latEst = float(estacion.get("latitud", 0))
            lngEst = float(estacion.get("longitud", 0))
            if latEst == 0 and lngEst == 0:
                continue
        except (ValueError, TypeError):
            continue 

        distancia = calcularDistancia(lat, lng, latEst, lngEst)
       
        servicios = estacion.get("servicios",[])
        tieneEstacion = len(servicios)>0
        estacionInfo= None

        if tieneEstacion:
            estacionInfo= {
                "CodigoTienda": str(servicios[0].get("id", "S/N")),
                "NombreTienda": "Servicio de Estación",
                "Tipo": "Convenio"
            }
        
        if store and not tieneEstacion:
            continue

        estacionNormalizada = {
            "CodEs": str(estacion.get("id", "")),
            "Compania": str(estacion.get("marca", "")), 
            "Direccion": str(estacion.get("direccion", "")),
            "Comuna": str(estacion.get("comuna", "")),
            "Region": str(estacion.get("region", "")),
            "Latitud": latEst,
            "Longitud": lngEst,
        }

        estacionesFiltradas.append({
            "data_original": estacionNormalizada,
            "distancia": distancia,
            "precio": precioProducto,
            "tiene_tienda": tieneEstacion,
            "tienda_info": estacionInfo
        })

    if not estacionesFiltradas:
        return None

    if cheapest:
        estacionesFiltradas.sort(key=lambda x: (x["precio"], x["distancia"]))
    else:
        estacionesFiltradas.sort(key=lambda x: x["distancia"])

    return estacionesFiltradas[0]
