class Estudiante:
    """
    Clase Estudiante que representa a un estudiante con su cédula y nombre.
    """
    def __init__(self, cedula: str, nombre_estudiante:str):
        self.cedula = cedula
        self.nombre_estudiante = nombre_estudiante

    def getnombre_estudiante(self) -> str:
        """Devuelve el nombre del estudiante."""
        return self.nombre_estudiante

    def getcedula(self) -> str:
        """Devuelve la cedula del estudiante."""
        return self.cedula