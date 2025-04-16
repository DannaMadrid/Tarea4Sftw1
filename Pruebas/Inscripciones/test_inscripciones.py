"""importando librerias necesarias para el test"""
import csv
import os
import tempfile
import unittest
from datetime import date
from Inscripciones.inscripciones import Estudiante, Materia, Inscripcion
from Inscripciones.inscripciones import ControlArchivoCSV

class TestInscripciones(unittest.TestCase):
    """Test para la clase Estudiante"""

    def test_calcular_total_materias(self):
        """Test para calcular el total de materias inscritas por cada estudiante."""
        estudiante1 = Estudiante("1234567", "Lulú López")
        estudiante2 = Estudiante("9876543", "Carlos Pérez")

        materia1 = Materia("1040", "Cálculo")
        materia2 = Materia("1050", "Física")

        inscripciones = [
            Inscripcion(estudiante1, materia1, date.today()),
            Inscripcion(estudiante1, materia2, date.today()),
            Inscripcion(estudiante2, materia1, date.today())
        ]

        contador = {}

        for ins in inscripciones:
            estudiante = ins.getestudiante()
            nombre = estudiante.getnombre_estudiante()
            contador[nombre] = contador.get(nombre, 0) + 1

        self.assertEqual(contador["Lulú López"], 2)
        self.assertEqual(contador["Carlos Pérez"], 1)


class TestControlArchivoCSV(unittest.TestCase):
    """Test para la clase ControlArchivoCSV que maneja la carga de datos desde un archivo CSV."""
    def test_cargar_datos(self):
        """Test para cargar datos desde un archivo CSV y contar materias por estudiante."""
        # Crear archivo temporal con datos de prueba
        with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False,
                                          encoding='utf-8') as temp_csv:
            writer = csv.writer(temp_csv)
            writer.writerow(["nombre_estudiante", "nombre_materia"])
            writer.writerow(["Lulú López", "Matemáticas"])
            writer.writerow(["Lulú López", "Física"])
            writer.writerow(["Pepito Pérez", "Química"])
            writer.writerow(["Calvin Clein", "Historia"])
            writer.writerow(["Calvin Clein", "Geografía"])
            ruta_temporal = temp_csv.name

        # Crear instancia del controlador y ejecutar método
        controlador = ControlArchivoCSV()
        resultado = controlador.cargar_datos(ruta_temporal)

        # Verificar resultados esperados
        esperado = [
            "Lulú López: 2 materias",
            "Pepito Pérez: 1 materias",
            "Calvin Clein: 2 materias"
        ]
        self.assertCountEqual(resultado, esperado)  # No importa el orden

        # Limpiar archivo temporal
        os.remove(ruta_temporal)


if __name__ == '__main__':
    unittest.main()
