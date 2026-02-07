'''
Programas relacionados al manejo y gesión de tareas, permite mostrar, agregar, marcar como finalizada o eliminar tareas.
'''

from src.utils.get_time import obtener_fecha
def mostrar_tareas(tareas):
    
    '''
    Muestra una lista de tareas pendientes.
    
    Si no hay tareas pendientes, se muestra un mensaje indicando que no hay tareas pendientes.
    De lo contrario, se muestra una lista con las tareas pendientes, incluyendo la fecha, descripción y si está finalizada o no.
    '''
    
    if not tareas:
        print("\nNo hay tareas pendientes.")
    else:
        print("\nTareas pendientes:")
        for i in range(len(tareas)):
            print(f"{i + 1}. fecha: {tareas[i]['fecha']}, descripcion: {tareas[i]['descripcion']}, finalizada: {'Sí' if tareas[i]['finalizada'] else 'No'}")
    
def agregar_tarea(tareas):
    
    '''
    Agrega una nueva tarea a la lista de tareas pendientes.
    
    La función obtiene la fecha actual y pide al usuario que ingrese la descripción de la nueva tarea.
    Luego, se crea un nuevo diccionario con la fecha y descripción ingresadas y se agrega a la lista de tareas pendientes.
    Por último, se muestra un mensaje indicando que la tarea se agregó exitosamente.
    '''
    
    fecha = obtener_fecha()
    descripcion = input("\nIngrese la descripción de la nueva tarea: ")
    nueva_tarea = {"fecha": fecha, "descripcion": descripcion, "finalizada": 0}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")
    
def terminar_tarea(tareas):
    
    '''
    Marca una tarea como finalizada.
    
    La función pide al usuario que ingrese el número de la tarea a marcar como finalizada.
    Si el usuario escribe 0, se muestra la lista de tareas pendientes nuevamente y se llama a la función nuevamente.
    Si el usuario ingresa un número válido, se marca la tarea correspondiente como finalizada.
    Si el usuario ingresa un número inválido, se muestra un mensaje indicando que el índice es inválido.
    '''
    
    indice = int(input("Ingrese el número de la tarea a marcar como finalizada o escriba 0 para mostrar la lista de tareas nuevamente: ")) - 1
    if indice == -1:
        mostrar_tareas(tareas)
        terminar_tarea(tareas)
    elif 0 <= indice < len(tareas):
        tareas[indice]['finalizada'] = 1
        print("\nTarea marcada como finalizada exitosamente.")
    else:
        print("Índice inválido.")


def eliminar_tareas_finalizadas(tareas):
    
    '''
    Elimina las tareas finalizadas de la lista de tareas pendientes.
    
    La función reemplaza la lista original con una nueva que solo contiene las tareas no finalizadas.
    Luego, se muestra un mensaje indicando que las tareas finalizadas se eliminaron exitosamente.
    '''
    
    tareas[:] = [n for n in tareas if not n['finalizada']] # Reemplazamos la lista original con una nueva que solo contiene las tareas no finalizadas
    print("\nTareas finalizadas eliminadas exitosamente.")
