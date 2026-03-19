# Importamos el modelo
from modelos.visitante import Visitante

# Clase que maneja la lógica del sistema (CRUD)
class VisitaServicio:
    def __init__(self):
        """
        Constructor del servicio
        Se crea una lista privada para almacenar visitantes
        """
        self.__visitantes = []

    def registrar_visitante(self, cedula, nombre, motivo):
        """
        Registra un nuevo visitante

        Retorna:
        True -> registro exitoso
        False -> cédula duplicada
        """

        # Validar que la cédula no esté repetida
        for v in self.__visitantes:
            if v.get_cedula() == cedula:
                return False

        # Crear objeto visitante
        nuevo = Visitante(cedula, nombre, motivo)

        # Agregar a la lista
        self.__visitantes.append(nuevo)

        return True

    def obtener_visitantes(self):
        """
        Retorna la lista de visitantes
        """
        return self.__visitantes

    def eliminar_visitante(self, cedula):
        """
        Elimina un visitante por cédula

        Retorna:
        True -> eliminado
        False -> no encontrado
        """
        for v in self.__visitantes:
            if v.get_cedula() == cedula:
                self.__visitantes.remove(v)
                return True

        return False