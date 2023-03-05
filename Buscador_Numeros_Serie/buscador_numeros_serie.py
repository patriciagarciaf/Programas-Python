import os
import re
from datetime import date
import time
import math

ruta = 'C:\\Users\\Propietario\\PycharmProjects\\programas-python\\Buscador_Numeros_Serie\\Mi_Gran_Directorio'

patron = r'N\D{3}-\d{5}'

print('-'*50)
print(f'Fecha de búsqueda: {date.today()}\n')
print('ARCHIVO\t\t\tNRO. SERIE')
print('-'*len('archivo') + '\t\t\t' + '-'*len('nro. serie'))
contador = 0

inicio = time.time()
for carpeta, subcarpeta, archivo in os.walk(ruta):
    for arch in archivo:
        ruta_archivo = carpeta + '\\' + arch
        ar = open(ruta_archivo, 'r')
        texto = ar.read()
        ar.close()
        num_serie = re.search(patron, texto)

        if num_serie is not None:
            print(f'{arch}\t{num_serie.group(0)}')
            contador += 1

final = time.time()

duracion = final - inicio

print(f'\nNúmeros encontrados: {contador}')
print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
print('-'*50)




