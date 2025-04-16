"""importando librerias necesarias para el test"""
import csv
import os
import tempfile
import unittest
from datetime import date
from controlArchivoCSV import ControlArchivoCSV
from controlProcesoInscripciones import ControlProcesoInscripcion
from inscripcion import Inscripcion
from estudiantes import Estudiante
from materia import Materia


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
    def setUp(self):
        self.control = ControlArchivoCSV()
    def test_0_archivo_valido(self):
        """Archivo CSV válido y completo.
        Comprueba que el método carga correctamente todos los datos cuando el archivo existe y tiene el formato esperado.
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV\valido.csv"

        # Crear instancia del controlador y ejecutar método
        controlador = ControlArchivoCSV()
        resultado = controlador.cargar_datos(ruta_archivo)

        # Verificar resultados esperados
        self.assertEqual(len(resultado), 5)
        # ✅ Verificamos los datos del primer objeto Inscripcion
        primera = resultado[0]
        self.assertEqual(primera.getEstudiante().getNombreEstudiante(), "Lulú López")
        self.assertEqual(primera.getEstudiante().getCedula(), "1234567")
        self.assertEqual(primera.getMateria().getCodigo(), "1040")
        self.assertEqual(primera.getMateria().getNombreMateria(), "Cálculo")

    def test_1_ruta_inexistente(self):
        """Test ruta de archivos inexistente"""
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV\noExiste.csv"

        with self.assertRaises(FileNotFoundError):
            self.control.cargar_datos(ruta_archivo)
    def test_2_archivo_vacio(self):
        """Test Archivo CSV vacío, es decir, el archivo existe pero no contiene ningún dato."""
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV\vacio.csv"
        resultado = self.control.cargar_datos(ruta_archivo)
        self.assertEqual(resultado, [])
    def test_3_archivo_datos_incompletos(self):
        """Test de archivo con datos incompletos donde falta algún campo en la línea CSV.
            En este caso supondremos que hay una línea así: “9876534,Pepito Pérez,1040 ”
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV\campoInvalido.csv"
        with self.assertRaises(Exception):
            self.control.cargar_datos(ruta_archivo)
    def test_4_campos_mal_formato(self):
        """Archivo con campos que no cumplen formato.
            En este caso supondremos que hay una línea así:“123456a,Lulú López,1040,Cálculo”
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV\campoInvalido.csv"
        with self.assertRaises(ValueError):
            self.control.cargarDatos(ruta_archivo)

    def test_5_archivo_lineas_duplicadas(self):
        """Archivo con líneas duplicadas. 
            En este caso supondremos que hay unas líneas así:
            “1234567,Lulú López,1060,Administración 
            1234567,Lulú López,1060,Administración”
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV\archivosCSV\lineasDuplicadas.csv"
        resultado = self.control.cargarDatos(ruta_archivo)
        self.assertEqual(len(resultado), 5)  # La línea duplicada aparece 2 veces
    def test_6_datos_nulos(self):
        """Archivo con líneas duplicadas. 
            En este caso supondremos que hay unas líneas así:
            “1234567,Lulú López,1060,Administración 
            1234567,Lulú López,1060,Administración”
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV\camposNulos.csv"
        with self.assertRaises(Exception):
            self.control.cargarDatos(ruta_archivo)
        


if __name__ == '__main__':
    unittest.main()
