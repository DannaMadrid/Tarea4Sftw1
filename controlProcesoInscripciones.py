from inscripcion import Inscripcion
class ControlProcesoInscripcion:
    """
    Clase que controla el proceso de inscripciones y calcula el total de materias por estudiante.
    """
    def __init__(self, inscripciones: list):
        self.inscripciones = inscripciones

    def calcular_total_materias(self) -> dict:
        """Calcula el total de materias inscritas por cada estudiante."""
        totales = {}
        for inscripcion in self.inscripciones:
            estudiante = inscripcion.getestudiante()
            nombre = estudiante.getnombreestudiante()
            if nombre in totales:
                totales[nombre] += 1
            else:
                totales[nombre] = 1
        return totales
