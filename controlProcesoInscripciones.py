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

    def calcular_total_inscripciones(self):
        """Calcula cuántas materias tiene cada estudiante."""
        contador = {}
        for inscripcion in self.inscripciones:
            estudiante = inscripcion.getestudiante()
            nombre = estudiante.getnombre_estudiante()
            contador[nombre] = contador.get(nombre, 0) + 1
        return contador
