# Lista de Tareas - Aplicación GUI con Tkinter

Aplicación de escritorio desarrollada en Python utilizando Tkinter, que permite gestionar tareas diarias mediante una interfaz gráfica interactiva. El sistema responde a eventos de teclado y ratón, permitiendo una interacción fluida por parte del usuario.

---

## Funcionamiento

La aplicación permite al usuario:

- Agregar nuevas tareas mediante un campo de texto
- Presionar la tecla Enter para añadir tareas rápidamente
- Marcar tareas como completadas mediante un botón o doble clic
- Eliminar tareas seleccionadas
- Visualizar el estado de cada tarea:
  - Rojo: tarea pendiente
  - Verde: tarea completada

La interfaz actualiza dinámicamente la lista de tareas según las acciones del usuario, proporcionando una retroalimentación visual clara.

---

## Estructura del Proyecto

El sistema está organizado bajo una arquitectura modular por capas:


lista_tareas_app/
│
├── main.py
├── modelos/
│   └── tarea.py
├── servicios/
│   └── tarea_servicio.py
├── ui/
│   └── app_tkinter.py
├── dist/
│   └── ListaTareas.exe
├── .gitignore


Autor:
Leiber Correa Bravo
