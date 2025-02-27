"""
Modulo que permite enrutar el archivo json correspondiente a la generacion de los datos
para tomar los parametros del modelo a definir tanto para las coordenadas como para 
el modelo del cliente.

"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "sample-data", "taxpayers.json")

