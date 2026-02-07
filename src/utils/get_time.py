'''
Programa para obtener la fecha y hora actual
'''

from datetime import datetime
def obtener_fecha():

    '''
    Obtiene la fecha y hora actual en formato string.
    
    La función devuelve un string con la fecha y hora actual en formato "dd/mm/yyyy hh:mm:ss".
    '''
    
    ahora = datetime.now()
    return ahora.strftime("%d/%m/%Y %H:%M:%S") # Devuelve la fecha y hora actual en formato "dd/mm/yyyy hh:mm:ss"

if __name__ == "__main__":
    print(f"La fecha y hora actual es: {obtener_fecha()}") # Verificamos que la función funciona correctamente