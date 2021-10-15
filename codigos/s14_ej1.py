# 
# Proyecto Final Curso de Python Intel
# 
# Alan Badillo Salas (dragonnomada123@gmail.com)
# 
# Este proyecto resuelve el problema de descargar un archivo zip
# desde un servidor y descomprimirlo.
# 
# Justificación:
# 
# ... Las empresas suelen tener repositorios zip con bases de datos excel
# 
# ... En mi empresa tenemos acceso a repositorios de imágenes comprimidas en zip
# para entrenar redes neuronales, ...
# 
# Descripción:
# 
# Vamos a utilizar la librería requests ...
# 
# Versión: Octubre 2021
# 

import requests

results = 5
page = 1
seed = "456"
nat = ["us", "gb", "fr"]

# 2. Lanzar la petición y obtener la respuesta
response = requests.get(f"https://randomuser.me/api?results={results}&page={page}&seed={seed}&nat={','.join(nat)}")

# 3. Obtenemos los resultados de la respuesta convertidos a un diccionario de python
data = response.json()

# print(data) # {'results': [{'gender': 'male', 'name': {'title': 'Mr', 'first': 'Jared', 'last': 'Caldwell'}, ...

for user in data["results"]:
    print(user["name"]["title"], user["name"]["first"], user["name"]["last"])
    print(user["gender"], user["email"])
    print("-" * 40)