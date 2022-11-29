import requests
import time
from bs4 import BeautifulSoup

time.sleep(60)

metodo='GET'
uri='http://servidor-caddy'
cabecera={'Host': 'servidor-caddy' }
respuesta=requests.request(metodo, uri, headers=cabecera, allow_redirects=True)

contenido = respuesta.content
document = BeautifulSoup(contenido, "html.parser")
titulos = document.find_all('p', {'class':'reemplazo'})

division1 = str(titulos[0]).split(">")
division_nombre = str(division1[1]).split("<")
nombre = str(division_nombre[0])

division2= str(titulos[1]).split(">")
division_apellido = str(division2[1]).split("<")
apellido = str(division_apellido[0])

division3 = str(titulos[2]).split(">")
division_dni = str(division3[1]).split("<")
dni = str(division_dni[0])


print("Los datos recogidos de la web son los siguientes:")
print("Nombre :" + nombre)
print("Apellido : " + apellido)
print("DNI : " + dni)

