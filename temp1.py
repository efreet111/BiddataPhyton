# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import os
import csv
import urllib3
mainpath = "C:/Users/Gantz/Documents/cursos/Machine Learning/python-ml-course/datasets"
filename = "titanic/titanic3.csv"
fullpath = os.path.join(mainpath, filename)
data = pd.read_csv(fullpath)
data.head()

medals_url = "http://winterolympicsmedals.com/medals.csv"
medals_data = pd.read_csv(medals_url)
medals_data.head()
    
http = urllib3.PoolManager()
r = http.request('GET', medals_url)
htmlSource = r.data
r.status
r.data
datos = r.data.decode('UTF-8')
lineas = datos.split("\n")

nombre_columnas = lineas[0].split(",")
num_col = len(nombre_columnas)


contador = 0
diccionario = {}
for columna in nombre_columnas:
    diccionario[columna] = [] #ya tenemos nuestras claves con su contenido vacio
    #IMPORTANTE
    #el diccionario se define con llaves {}
    #las listas se defines con corchetes []
    #el diccionario en cada clave guarda una lista de datos (porque lo hemos definido asi)
    #si definimos la lista de dentro como {} será diccionario y no podremos llamar a dict.append
diccionario
for linea in lineas:
    if(contador > 0): #con esto nos saltamos la fila 0 (cabecera)
        valores = linea.strip().split(",")
        #recuerda: strip retira caracteres de espacio en blanco por defecto
        #ahora añadimos cada valor a su columna
        for i in range(len(nombre_columnas)):
            diccionario[nombre_columnas[i]].append(valores[i])
    contador += 1
    
print("El data set tiene %d filas y %d columnas" % (contador, num_col))

medallas_df = pd.DataFrame(diccionario)
medallas_df.head()    