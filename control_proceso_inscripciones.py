"""
Módulo que contiene la clase ControlProcesoInscripcion, que gestiona el proceso de inscripciones
"""
class ControlProcesoInscripcion:
    # implementación
    """
    Clase que controla el proceso de inscripciones y calcula el total de materias por estudiante.
    """
    def __init__(self, inscripciones: list):
        self.inscripciones = inscripciones

    def calcular_total_materias(self) -> dict:
        """
        Calcula el total de materias inscritas por cada estudiante.
        Retorna un diccionario con la cédula como clave y una tupla (nombre, total_materias)"""
        totales = {}

        for  inscripcion in self.inscripciones:
            estudiante = inscripcion.getestudiante()
            cedula = estudiante.getcedula()
            nombre = estudiante.getnombre_estudiante()

            if cedula in totales:
                totales[cedula]['total'] += 1
            else:
                totales[cedula] = {'nombre': nombre, 'total': 1}

        return totales
