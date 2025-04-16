
"""
Este módulo contiene la lógica para gestionar el proceso de inscripción
de estudiantes a las actividades académicas.
"""
from estudiantes import Estudiante
from materia import Materia

class Inscripcion:
    """
    Clase que representa la inscripción de un estudiante a una materia en una fecha específica. 
    """
    def __init__(self, estudiante: Estudiante, materia: Materia):
        self.estudiante = estudiante
        self.materia = materia

    def getestudiante(self) -> Estudiante:
        """Devuelve el objeto Estudiante asociado a la inscripción."""
        return self.estudiante

    def getmateria(self) -> Materia:
        """Devuelve el objeto Materia asociado a la inscripción."""
        return self.materia
