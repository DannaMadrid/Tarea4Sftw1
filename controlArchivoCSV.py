import csv
from typing import List
from inscripcion import Inscripcion
from estudiantes import Estudiante
from materia import Materia

class ControlArchivoCSV: 
    """
    Clase que controla la carga de datos desde un archivo CSV y valida su formato.
    """
    def cargar_datos(self, ruta_archivo:str) -> List[Inscripcion]:
        inscripciones = []

        with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)

            for fila in lector:
                if len(fila) != 4:
                    raise ValueError("Cada fila debe de tener 4 campos")
                cedula = fila[0].strip()
                nombre_estudiante = fila [1].strip()
                codigo_materia = fila[2].strip()
                nombre_materia = fila[3].strip()

                if not cedula.isdigit():
                    raise ValueError(f"Cédula inválida: {cedula}")

                if not codigo_materia.isdigit():
                    raise ValueError(f"Código de materia inválido: {codigo_materia}")

                estudiante = Estudiante(cedula, nombre_estudiante)
                materia = Materia(codigo_materia, nombre_materia)
                inscripcion = Inscripcion(estudiante, materia)

                inscripciones.append(inscripcion)
            return inscripciones
    def validar_archivo(self, ruta_archivo: str) -> bool:
        """Valida si el archivo tiene la extensión CSV."""

        return ruta_archivo.endswith(".csv")
    def buscar_ruta_archivo(self) -> str:
        # Método simulado, normalmente se obtendría por entrada del usuario o búsqueda automática
        """Bucar la ruta del archivo CSV."""

        return "datos.csv"