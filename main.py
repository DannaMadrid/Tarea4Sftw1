"""importando clases necesarias para el programa"""
from controlArchivoCSV import ControlArchivoCSV
from controlProcesoInscripciones import ControlProcesoInscripcion

class Main:
    """Clase principal que ejecuta el programa."""

    def ejecutar(self):
        """Método que ejecuta el programa."""
        ruta = input("Ingrese la ruta del archivo CSV: ").strip()

        try:
            # Cargar datos
            controlador_csv = ControlArchivoCSV()
            inscripciones = controlador_csv.cargar_datos(ruta)

            # Calcular total de materias por estudiante
            controlador_proceso = ControlProcesoInscripcion(inscripciones)
            resultado = controlador_proceso.calcular_total_inscripciones()

            # Mostrar resultados
            print("\nCantidad de materias por estudiante:")
            for estudiante, total in resultado.items():
                print(f"{estudiante}: {total} materias")

        except FileNotFoundError:
            print("❌ Error: No se encontró el archivo.")
        except ValueError as ve:
            print(f"❌ Error de formato: {ve}")
        except IOError as e:
            print(f"❌ Error inesperado: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    app = Main()
    app.ejecutar()
