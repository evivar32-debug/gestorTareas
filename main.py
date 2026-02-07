from src.services.task_services import mostrar_tareas, agregar_tarea, terminar_tarea, eliminar_tareas_finalizadas

TAREAS_INICIALES = [{"fecha": "02/01/2026 10:25:32", "descripcion": "Enviar correo a Azura S.A", "finalizada": False},
                     {"fecha": "02/01/2026 12:00:00", "descripcion": "Reunión con el equipo de desarrollo", "finalizada": False},
                     {"fecha": "02/01/2026 15:30:00", "descripcion": "Preparar presentación para el cliente", "finalizada": False}]

def main():
    tareas = 0 # Agregar codigo para leer tareas desde un archivo
    if not tareas:
        tareas = TAREAS_INICIALES
    while True:
        if not tareas:
            print("¡Felicidades! No tienes tareas pendientes.")
            break
        print("\nMenú de Tareas:")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Terminar tarea")
        print("4. Eliminar tareas finalizadas")
        print("5. Salir")
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
                    print("Saliendo...")
                    break
                case _:
                    print("Opción inválida. Por favor intente de nuevo.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            
if __name__ == "__main__":
    main()