from typing import List

from API import DATA_PATH, ModeloCliente, clientes_seleccionados
from fastapi import FastAPI, Query

app = FastAPI()

#EndPoint donde vamos a acceder para obtener nuestra respuesta con FastAPI
@app.get("/clientes-seleccionados", response_model=List[ModeloCliente])

def seleccion_clientes(
    
    #Las entradas de la latitud y longitud no seran estaticas por lo que se asignan en la URL
    latid_coord: float = Query(..., description="Latitud de fixat"),
    long_coord: float = Query(..., description="Longitud de fixat")
):
    
    
    
    top = clientes_seleccionados(DATA_PATH, latid_coord, long_coord, elegidos=10)
    return top

if __name__ == "__main__":
    
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
    
