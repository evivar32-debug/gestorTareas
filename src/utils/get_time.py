from datetime import datetime
def obtener_fecha():
    # 1. Obtenemos el objeto con la fecha y hora exacta de este momento
    ahora = datetime.now()

    # 2. Aplicamos el formato que solicitaste
    # %d: día, %m: mes, %Y: año (4 dígitos)
    # %H: hora, %M: minutos, %S: segundos
    return ahora.strftime("%d/%m/%Y %H:%M:%S")

if __name__ == "__main__":
    print(f"La fecha y hora actual es: {obtener_fecha()}") # Verificamos que la función funciona correctamente