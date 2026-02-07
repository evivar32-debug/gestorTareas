# Gestor de Tareas CLI (Command Line Interface)

## 1. Descripción del Proyecto
Este proyecto consiste en una aplicación de consola desarrollada en **Python** para la gestión eficiente de tareas personales. El sistema permite a los usuarios crear, visualizar, completar y eliminar tareas, implementando **persistencia de datos** mediante archivos CSV.

El objetivo principal es demostrar la manipulación de estructuras de datos (listas de diccionarios), el manejo de archivos de texto plano y la modularización del código en una arquitectura escalable.

## 2. Requisitos del Sistema
Para ejecutar este proyecto se requiere:
* **Lenguaje:** Python 3.6 o superior.
* **Librerías:** Solo utiliza librerías estándar de Python (`csv`, `os`, `datetime`), por lo que no requiere instalación de paquetes externos (`pip`).
* **Sistema Operativo:** Compatible con Windows, macOS y Linux.

## 3. Instalación y Ejecución
Siga estos pasos para poner en marcha la aplicación:

1.  **Descomprimir el proyecto** en su directorio de preferencia si se descarga en formato zip.
2.  Abrir una terminal o línea de comandos.
3.  Navegar hasta la carpeta raíz del proyecto `gestorTareas`.
4.  Ejecutar el archivo principal:

```bash
python main.py
```
## 5. Estructura del Proyecto
El proyecto está organizado de la siguiente manera:



* **main.py:** Punto de entrada y gestión del menú interactivo.
* **src/data/tareas.csv:** Base de datos en formato plano.
* **src/services/task_services.py:** Lógica de manipulación de la lista de tareas.
* **src/utils/data_manager.py:** Funciones de lectura y escritura en CSV.
* **src/utils/get_time.py:** Generador de formato de fecha.

## 6. Documentación de Módulos

### 6.1. Lógica Principal (`main.py`)
Coordina el inicio del programa cargando datos del CSV. Si no hay datos previos, inicializa el sistema con `TAREAS_INICIALES` para facilitar la evaluación. Gestiona el ciclo de vida del menú mediante un bucle `while`.

### 6.2. Servicios (`task_services.py`)
* **`mostrar_tareas`**: Formatea la salida en consola y traduce el estado `0/1` a "Sí/No".
* **`agregar_tarea`**: Crea el objeto tarea y lo anexa a la lista global.
* **`terminar_tarea`**: Localiza una tarea por índice y cambia su estado a finalizada.
* **`eliminar_tareas_finalizadas`**: Limpia la lista usando `tareas[:]` para modificar la referencia original.

### 6.3. Gestión de Datos (`data_manager.py`)
* **Lectura**: Utiliza `csv.DictReader` para mapear el archivo a diccionarios de Python.
* **Escritura**: Implementa `csv.DictWriter`, asegurando que los encabezados se escriban correctamente en cada guardado.

### 6.4. Utilidad de Tiempo (`get_time.py`)
Estandariza el formato de fecha como `dd/mm/yyyy HH:MM:SS` usando el módulo `datetime`.

## 7. Formato del Archivo CSV
El archivo de persistencia utiliza el siguiente esquema:



| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| **fecha** | String | Fecha de creación. |
| **descripcion** | String | Detalle de la tarea. |
| **finalizada** | Integer | `0` (Pendiente) / `1` (Hecha). |

---
**Autor:** [Elvis Vivar]
**Fecha:** Febrero 2026
