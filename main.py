# Importamos las funciones necesarias desde los módulos correspondientes
from src.services.task_services import mostrar_tareas, agregar_tarea, terminar_tarea, eliminar_tareas_finalizadas
from src.utils.data_manager import leer_tareas, guardar_tareas

# Definimos una lista de tareas iniciales para usar en caso de que no existan tareas guardadas en el archivo CSV.
# Cada tarea es un diccionario con las claves 'fecha', 'descripcion' y 'finalizada'. La clave 'finalizada' se representa como 
# un entero (0 para no finalizada, 1 para finalizada) para mantener consistencia con el formato de tareas utilizado en el archivo CSV.
TAREAS_INICIALES = [{"fecha": "02/01/2026 10:25:32", "descripcion": "Enviar correo a Azura S.A", "finalizada": 0},
                     {"fecha": "02/01/2026 12:00:00", "descripcion": "Reunión con el equipo de desarrollo", "finalizada": 0},
                     {"fecha": "02/01/2026 15:30:00", "descripcion": "Preparar presentación para el cliente", "finalizada": 0}]

def main(): 
    
    '''
    Leemos primero las tareas guardadas si es que existen, en caso contrario se asignan las tareas iniciales para trabajar, esto
    es meramente didactico, se puede saltar esta parte si se desea.
    Se despliega un menu para que el usuario pueda gestionar tareas segun lo requiera y guardar los datos si se requiere. 
    '''
    
    tareas = leer_tareas()
    # Comentar las siguientes 3 lineas si no se desea asignar valores iniciales
    if not tareas:
        print("Se escribiran tareas de prueba")
        tareas = TAREAS_INICIALES 
    
    while True:
        print("\nMenú de Tareas:")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Terminar tarea")
        print("4. Eliminar tareas finalizadas")
        print("5. Guardar tareas")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        try:
            match opcion:
                case "1":
                    mostrar_tareas(tareas)
                case "2":
                    agregar_tarea(tareas)
                case "3":
                    terminar_tarea(tareas)
                case "4":
                    eliminar_tareas_finalizadas(tareas)
                case "5":
                    guardar_tareas(tareas)
                case "6":
                    print("Saliendo...")
                    break
                case _:
                    print("Opción inválida. Por favor intente de nuevo.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            
if __name__ == "__main__":
    main()