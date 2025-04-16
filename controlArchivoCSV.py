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
        filas_vistas = set()

        with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)

            for fila in lector:
                if len(fila) != 4:
                    raise ValueError("Cada fila debe de tener 4 campos")
                
                 # Crear la tupla con todos los campos
                fila_normalizada = tuple(campo.strip() for campo in fila)

                # Validar campos nulos (vacíos)
                if any(campo == "" for campo in fila_normalizada):
                    raise ValueError("Uno o más campos están vacíos (nulos) en la fila.")

                if fila_normalizada in filas_vistas:
                    continue  # Salta si la fila ya se había visto

                filas_vistas.add(fila_normalizada)

                cedula, nombre_estudiante, codigo_materia, nombre_materia = fila_normalizada

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

            # Mostrar los resultados para revisión visual
            print("\n📄 Inscripciones cargadas:")
            for i, ins in enumerate(inscripciones, 1):
                print(f"{i}. Estudiante: {ins.getestudiante().getnombre_estudiante()} | "
                f"Cédula: {ins.getestudiante().getcedula()} | "
                f"Materia: {ins.getmateria().getnombre_materia()} | "
                f"Código: {ins.getmateria().getcodigo()}")

            return inscripciones
    def validar_archivo(self, ruta_archivo: str) -> bool:
        """Valida si el archivo tiene la extensión CSV."""

        return ruta_archivo.endswith(".csv")
    def buscar_ruta_archivo(self) -> str:
        # Método simulado, normalmente se obtendría por entrada del usuario o búsqueda automática
        """Bucar la ruta del archivo CSV."""

        return "datos.csv"