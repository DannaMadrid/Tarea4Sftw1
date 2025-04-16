""" importar las librerías necesarias """
from controlArchivoCSV import ControlArchivoCSV

def main():
    """función principal del programa"""
    print("=== SISTEMA DE INSCRIPCIÓN ===")
    ruta = input("Ingrese la ruta del archivo CSV: ")

    controlador = ControlArchivoCSV()

    try:
        # Cargar las inscripciones desde el archivo CSV
        inscripciones = controlador.cargar_datos(ruta)

        # Verificar si el archivo estaba vacío
        if not inscripciones:
            print("El archivo está vacío o no contiene inscripciones.")
            return

        # Contar las materias por estudiante
        contador = {}
        for ins in inscripciones:
            estudiante = ins.getestudiante()
            nombre = estudiante.getnombre_estudiante()
            contador[nombre] = contador.get(nombre, 0) + 1

        # Mostrar la cantidad de materias por estudiante
        print("\nCantidad de materias inscritas por estudiante:\n")
        for nombre, total in contador.items():
            print(f"{nombre}: {total} materias")

    except FileNotFoundError:
        print("Error: El archivo no fue encontrado. Verifique la ruta.")
    except ValueError as ve:
        print(f"Error de datos: {ve}")
    except IOError:
        print("Error de entrada/salida al intentar leer el archivo.")

if __name__ == "__main__":
    main()
