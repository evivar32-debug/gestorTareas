TAREAS_INICIALES = ["Ir a la supermercado", "Comprar ingredientes", "Preparar la cocina"]

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i in range(len(tareas)):
            print(f"{i + 1}. {tareas[i]}")
    return

def agregar_tarea(tareas):
    nueva_tarea = input("Ingrese la nueva tarea: ")
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")
    return

def eliminar_tarea(tareas):
    indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        print("Tarea eliminada exitosamente.")
    else:
        print("Índice inválido.")

def main():
    tareas = TAREAS_INICIALES
    while True:
        if not tareas:
            print("¡Felicidades! No tienes tareas pendientes.")
            break
        print("\nMenú de Tareas:")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        try:
            match opcion:
                case "1":
                    mostrar_tareas(tareas)
                case "2":
                    agregar_tarea(tareas)
                case "3":
                    eliminar_tarea(tareas)
                case "4":
                    print("Saliendo...")
                    break
                case _:
                    print("Opción inválida. Por favor intente de nuevo.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()  