from src.utils.get_time import obtener_fecha
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i in range(len(tareas)):
            print(f"{i + 1}. fecha: {tareas[i]['fecha']}, descripcion: {tareas[i]['descripcion']}, finalizada: {'Sí' if tareas[i]['finalizada'] else 'No'}")
    
def agregar_tarea(tareas):
    fecha = obtener_fecha()
    descripcion = input("Ingrese la descripción de la nueva tarea: ")
    nueva_tarea = {"fecha": fecha, "descripcion": descripcion, "finalizada": False}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")
    
def terminar_tarea(tareas):
    indice = int(input("Ingrese el número de la tarea a marcar como finalizada o escriba 0 para mostrar la lista de tareas nuevamente: ")) - 1
    if indice == -1:
        mostrar_tareas(tareas)
        terminar_tarea(tareas)
    elif 0 <= indice < len(tareas):
        tareas[indice]['finalizada'] = True
        print("Tarea marcada como finalizada exitosamente.")
    else:
        print("Índice inválido.")

def eliminar_tareas_finalizadas(tareas):
    tareas[:] = [n for n in tareas if not n['finalizada']] # Reemplazamos la lista original con una nueva que solo contiene las tareas no finalizadas
    print("Tareas finalizadas eliminadas exitosamente.")
