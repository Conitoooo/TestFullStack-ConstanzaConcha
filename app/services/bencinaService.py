import httpx

URL_Busqueda = "https://api.bencinaenlinea.cl/api/busqueda_estacion_filtro"

async def obtenerEstaciones():
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "Accept":"application/json"
    }

    async with httpx.AsyncClient() as client:
        try:
            response= await client.get(URL_Busqueda,headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as exc:
            print(f"error al comunnicarse con la Api de bencina {exc}")
            return[]
        except Exception as exc:
            print(f"Error {exc}")
            return[]

