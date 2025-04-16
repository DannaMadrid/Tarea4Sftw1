"""
Módulo para procesar archivos CSV relacionados con inscripciones de estudiantes.
"""
import csv
from datetime import  datetime


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


class Inscripcion:
    """
    Clase que representa la inscripción de un estudiante a una materia en una fecha específica. 
    """
    def __init__(self, estudiante: Estudiante, materia: Materia, fecha_inscripcion: datetime.date):
        self.estudiante = estudiante
        self.materia = materia
        self.fecha_inscripcion = fecha_inscripcion

    def getestudiante(self) -> Estudiante:
        """Devuelve el objeto Estudiante asociado a la inscripción."""
        return self.estudiante

    def getmateria(self) -> Materia:
        """Devuelve el objeto Materia asociado a la inscripción."""
        return self.materia

    def getfecha_inscripcion(self) -> datetime.date:
        """Devuelve la fecha de inscripción."""
        return self.fecha_inscripcion

class ControlProcesoInscripciones:
    """
    Clase que controla el proceso de inscripciones y calcula el total de materias por estudiante.
    """
    def __init__(self, inscripciones: list):
        self.inscripciones = inscripciones

    def calcular_total_materias(self) -> dict:
        """Calcula el total de materias inscritas por cada estudiante."""
        totales = {}
        for inscripcion in self.inscripciones:
            estudiante = inscripcion.getEstudiante()
            nombre = estudiante.getNombreEstudiante()
            if nombre in totales:
                totales[nombre] += 1
            else:
                totales[nombre] = 1
        return totales


class ControlArchivoCSV:
    """
    Clase que controla la carga de datos desde un archivo CSV y valida su formato.
    """
    def cargar_datos(self, ruta_archivo):
        """Carga los datos desde un archivo CSV y cuenta las materias por estudiante."""

        conteo_inscripciones = {}
        with open(ruta_archivo, newline='', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                estudiante = fila["nombre_estudiante"]
                conteo_inscripciones[estudiante] = conteo_inscripciones.get(estudiante, 0) + 1
        resultado = [f"{nombre}: {cantidad} materias" 
                     for nombre,cantidad in conteo_inscripciones.items()]
        return resultado
    def validar_archivo(self, ruta_archivo: str) -> bool:
        """Valida si el archivo tiene la extensión CSV."""

        return ruta_archivo.endswith(".csv")
    def buscar_ruta_archivo(self) -> str:
        # Método simulado, normalmente se obtendría por entrada del usuario o búsqueda automática
        """Bucar la ruta del archivo CSV."""

        return "datos.csv"
