# Clase que representa una tarea individual
class Tarea:
    def __init__(self, id, descripcion):
        # Atributos privados (encapsulamiento)
        self._id = id
        self._descripcion = descripcion
        self._completada = False

    # GETTERS
    def get_id(self):
        """Retorna el ID de la tarea"""
        return self._id

    def get_descripcion(self):
        """Retorna la descripción de la tarea"""
        return self._descripcion

    def get_completada(self):
        """Retorna el estado de la tarea (True/False)"""
        return self._completada

    # SETTERS
    def set_descripcion(self, nueva_descripcion):
        """Modifica la descripción de la tarea"""
        self._descripcion = nueva_descripcion

    def set_completada(self, estado):
        """Cambia el estado de la tarea"""
        self._completada = estado

    # Método adicional
    def marcar_completada(self):
        """Marca la tarea como completada"""
        self._completada = True