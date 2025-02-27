
#Modulo donde definimos la distancia manhattan 

import math


def distancia_manhattan(lat1, lon1, lat2, lon2):
    
    # 1 grado de latitud = aproximadamente 111 km
    valor_grado_latitud = 111 
    distancia_latitud = abs(lat1 - lat2) * valor_grado_latitud
    distancia_longitud = abs(lon1 - lon2) * (valor_grado_latitud * math.cos(math.radians(lat1)))  # tambien se ajusta la longitud
    return distancia_latitud + distancia_longitud  # Retornamos la distancia en km

