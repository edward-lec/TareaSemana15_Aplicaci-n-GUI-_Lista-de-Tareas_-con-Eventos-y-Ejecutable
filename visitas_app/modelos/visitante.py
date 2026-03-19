# Clase que representa la entidad Visitante (Modelo)
class Visitante:
    def __init__(self, cedula, nombre, motivo):
        """
        Constructor de la clase Visitante
        Se inicializan los atributos como privados (encapsulamiento)
        """
        self.__cedula = cedula
        self.__nombre = nombre
        self.__motivo = motivo

    # GETTERS

    def get_cedula(self):
        """Retorna la cédula del visitante"""
        return self.__cedula

    def get_nombre(self):
        """Retorna el nombre del visitante"""
        return self.__nombre

    def get_motivo(self):
        """Retorna el motivo de la visita"""
        return self.__motivo

    # SETTERS

    def set_cedula(self, cedula):
        """Modifica la cédula del visitante"""
        self.__cedula = cedula

    def set_nombre(self, nombre):
        """Modifica el nombre del visitante"""
        self.__nombre = nombre

    def set_motivo(self, motivo):
        """Modifica el motivo de la visita"""
        self.__motivo = motivo