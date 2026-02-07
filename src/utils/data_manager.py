'''
Programas relacionados al manejo de datos, permite guardar o leer datos en un archivo CSV en una ruta definida por la variable
ARCHIVO_CSV, se puede modificar la ruta si se quiere guardar los datos en otro directorio.
'''
import csv
import os

ARCHIVO_CSV = 'src/data/tareas.csv' # Ruta del archivo .csv


def leer_tareas():
    
    '''
    Programa para leer los datos guardados en el archivo .csv
    
    Si no existe el archivo .csv, retorna una lista vacia
    Lee el archivo .csv y retorna una lista de diccionarios con las tareas
    '''

    if not os.path.exists(ARCHIVO_CSV):     # Si no existe el archivo .csv, retorna una lista vacia
        print("No existen tareas guardadas.")
        return [] 
    try:
        with open(ARCHIVO_CSV, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            tareas = [] 
            for fila in lector:
                tarea = {
                    'fecha': fila['fecha'],
                    'descripcion': fila['descripcion'],
                    'finalizada': int(fila['finalizada'])  # Convertimos el valor de 'finalizada' a entero
                }
                tareas.append(tarea)
            return tareas
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return []

def guardar_tareas(tareas):
    
    '''
    Programa para guardar los datos en el archivo .csv
    
    Si la lista de tareas esta vacia, no se guarda nada
    Si la lista de tareas no esta vacia, se guarda en el archivo .csv con los campos 'fecha', 'descripcion' y 'finalizada'
    '''
    
    if not tareas:
        print("No hay tareas para guardar.")
        return
    try:
        with open(ARCHIVO_CSV, mode='w', newline='', encoding='utf-8') as archivo:
            campos = ['fecha', 'descripcion', 'finalizada'] # Claves del diccionario
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for tarea in tareas:
                escritor.writerow(tarea)
            print("\nTareas guardadas exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")
    