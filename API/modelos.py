"""
Modulo para definir las clases que contengan los modelos de latitude y longitude y los parametros
del modelo del cliente. 

"""

from pydantic import BaseModel

#Ponderaciones demograficas 

"""
edad: 10%
distancia a la oficina: 10%

"""

class FixOLocation(BaseModel): #Fixat Office location 
     
     latitude: float
     longitude: float

"""     
Clase para definir el modelo del cliente y utilizar los parametros para despues calcular
las distancias tomando la latitud y longitud
"""
class ModeloCliente(BaseModel):
    
    id: str
    name: str
    location: FixOLocation
    age: int
    accepted_offers: int
    canceled_offers: int
    average_reply_time: int 
    puntaje: float = 0.0