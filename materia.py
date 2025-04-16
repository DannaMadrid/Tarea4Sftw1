
class Materia:
    """
     Clase Materia que representa una materia con su código y nombre.
    """
    def __init__(self, codigo_materia: str, nombre_materia: str):
        self.codigo = codigo_materia
        self.nombre = nombre_materia

    def getcodigo(self) -> str:
        """Devuelve el código de la materia."""
        return self.codigo

    def getnombre_materia(self) -> str:
        """Devuelve el nombre de la materia."""
        return self.nombre