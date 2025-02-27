
"""
Modulo de servicios donde se realiza el calculo de la distancia, el puntaje, de definen ponderaciones, 
se cargan los datos y hace uso de dependencias como utils.py y modelos.py.

Se realiza normalizacion de datos para una mejor visualizacion de estos tanto para edad, distancia, 
tiempo de respuesta y el puntaje final. 

"""

import json
from typing import List

from API.modelos import ModeloCliente
from API.utils import distancia_manhattan

"""
-- Ponderaciones de comportamiento --

nunmero de ofertas aceptadas: 30%
numero de ofertas canceladas: 30% 
tiempo de respuesta (el tiempo que toma a los clientes dar una respuesta): 20%

"""

#Funcion que nos permite cargar el json correspondiente a los datos generados 
def cargar_clientes(ruta_json: str) -> List[ModeloCliente]:
    with open(ruta_json, "r") as f:
        data = json.load(f)
    return [ModeloCliente(**item) for item in data]

#Calculo del puntaje tomando como parametros el modelo del cliente previamente creado y coordenada de latitud y longitud
def calcular_puntuacion(modelo_cliente: ModeloCliente, latid_coord: float, long_coord: float) -> float:
    
    #Ponderaciones demograficas 
    
    ponderacion_edad = 0.10
    
    #Tomando valores maximos y minimos en la edad del json generado
    # max: 90, min: 18
    edad_normalizada = (90 - modelo_cliente.age) / (72) #90 - 18
    
    poderacion_distancia_oficina = 0.10
    distancia = distancia_manhattan(modelo_cliente.location.latitude, modelo_cliente.location.longitude, latid_coord, long_coord)
    
    #Debug de distancia
    # print(f"Cliente: {modelo_cliente.name}, Lat: {modelo_cliente.location.latitude}, Long: {modelo_cliente.location.longitude}, Distancia: {distancia}")
    

    normalizacion_distancia = max(0, 1 - (distancia /1000))  

    
    #Ponderaciones de comportamiento 
    
    ofertas_aceptadas = 0.30
    ofertas_canceladas = 0.30 
    tiempo_respuesta = 0.20
    

    #Calculamos la diferencia entre ofertas aceptadas y canceladas 
    total_ofertas = modelo_cliente.accepted_offers + modelo_cliente.canceled_offers
    #Dividimos la diferencia de ofertas aceptadas y canceladas entre el total de ofertas
    rango_de_aceptacion = max(0, (modelo_cliente.accepted_offers - modelo_cliente.canceled_offers) / max(total_ofertas, 1))
    #Penalizacion para ofertas canceladas y enfocar la puntuacion mas hacia las ofertas aceptadas
    penalizacion_cancelaciones = modelo_cliente.canceled_offers / max(total_ofertas, 1)
    #Normalizacion para el tiempo de respuesta mayor que el valor de la ponderacion 
    normalizacion_tiempo_respuesta = max(0, 1 - (modelo_cliente.average_reply_time / 3000))
    
    puntuacion_final = (
        
        (ponderacion_edad * edad_normalizada)+ 
        (poderacion_distancia_oficina * normalizacion_distancia) +
        (ofertas_aceptadas * rango_de_aceptacion) - 
        (ofertas_canceladas * penalizacion_cancelaciones) +
        (tiempo_respuesta * normalizacion_tiempo_respuesta)
        
    )
    """Puntuacion final obtenida de las sumas de las normalizaciones para:
        - edad
        - distancia a oficina
        - ofertas aceptadas
        - ofertas canceladas
        - tiempo de respuesta 
    """
    
    #Valor de puntaje redondeado despues de la normalizacion y multiplicando por 15 para no obtener valores bajos
    return round(max(1, min(10, puntuacion_final * 15)))


def clientes_seleccionados(ruta_json: str, latid_coord: float, long_coord: float, elegidos: int=10) -> List[ModeloCliente]:
    
    clientes_fixat = cargar_clientes(ruta_json)
    
    for cliente in clientes_fixat:
        cliente.puntaje = calcular_puntuacion(cliente, latid_coord, long_coord)
    
    #Devolver las puntuacioes calculadas y ordenadas
    return sorted(clientes_fixat, key=lambda x: x.puntaje, reverse=True)[:elegidos]
        

    
        
    
    