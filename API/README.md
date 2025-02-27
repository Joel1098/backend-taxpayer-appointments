## Definicion de problema 
El problema dicta que se pierde tiempo al encontrar clientes que en ocasiones no están disponibles 
o no contestan telefonos. 

## Definicion de solucion al problema 

Generar una lista que pueda aumentar las posibilidades de encontrar un cliente en las primeras llamadas.

## Características de la solución

Datos historicos de clientes y calcular su puntuacion por cada uno:

1 → la más baja
10 → la más alta

esto representará la probabilidad de que un cliente acepte la oferta de la lista de espera.

## Modelo de solucion:

Seperacion de dependencias modularizando para una mejor estructura de la solucion y con ello 
tener un control en la funcionalidad de cada archivo. 

## Version de python para entorno de ejecucion:
- 3.11.6

## Tecnologia:
- FastAPI

## librerias:
1. pydantic: para definicion de modelos a usar o reusar 
2. fastapi: para cargar datos de un archivo json 

## Modulos estandar:
1. typing 
2. json 
3. os 

## Funcionalidad de la API para mostrar la lista de clientes

1. Ingresar a la carpeta backend-taxpayer-appointments
2. Ejecutar el comando uvicorn API.main:app --reload --port 8000
3. El json con la lista de clientes se muestra en la siguiente URL:

http://127.0.0.1:8000/clientes-seleccionados?latid_coord=19.3797208&long_coord=-99.1940332&force_reload=true 

donde los valores latid_coord y long_coord tienen los valores de ejemplo proporcionados en el archivo
README.md de la prueba tecnica. 
