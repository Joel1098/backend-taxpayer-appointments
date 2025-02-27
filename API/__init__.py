"""
Constructor que nos permite definir las dependencias a utilizar dentro del proyecto 
modulado en python.

"""

from .data import DATA_PATH
from .modelos import FixOLocation, ModeloCliente
from .servicios import (calcular_puntuacion, cargar_clientes,
                        clientes_seleccionados)
from .utils import distancia_manhattan
