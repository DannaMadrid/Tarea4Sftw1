"""importando librerias necesarias para el test"""
import unittest
from control_archivo_CSV import ControlArchivoCSV
from control_proceso_inscripciones import ControlProcesoInscripcion

class TestControlArchivoCSV(unittest.TestCase):

    """Test para la clase ControlArchivoCSV que maneja la carga de datos desde un archivo CSV."""

    def setUp(self):
        self.control_csv = ControlArchivoCSV()

    def test_0_archivo_valido(self):
        """Verifica que el método cargue correctamente los datos de un archivo CSV válido."""
    # Ruta del archivo de prueba
        ruta_archivo = "archivosCSV/valido.csv"


        # Crear instancia del controlador y ejecutar método
        controlador = ControlArchivoCSV()
        resultado = controlador.cargar_datos(ruta_archivo)

        # Verificar resultados esperados
        self.assertEqual(len(resultado), 5)
        # Verifica los datos del primer objeto Inscripcion
        primera = resultado[0]
        self.assertEqual(primera.getestudiante().getnombre_estudiante(), "Lulú López")
        self.assertEqual(primera.getestudiante().getcedula(), "1234567")
        self.assertEqual(primera.getmateria().getcodigo(), "1040")
        self.assertEqual(primera.getmateria().getnombre_materia().strip(), "Cálculo")

    def test_1_ruta_inexistente(self):
        """Test ruta de archivos inexistente"""
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV/noExiste.csv"

        with self.assertRaises(FileNotFoundError):
            self.control_csv.cargar_datos(ruta_archivo)
    def test_2_archivo_vacio(self):
        """Test Archivo CSV vacío, es decir, el archivo existe pero no contiene ningún dato."""
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV/vacio.csv"
        resultado = self.control_csv.cargar_datos(ruta_archivo)
        self.assertEqual(resultado, [])
    def test_3_archivo_datos_incompletos(self):
        """Test de archivo con datos incompletos donde falta algún campo en la línea CSV.
            En este caso supondremos que hay una línea así: “9876534,Pepito Pérez,1040 ”
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV/campoInvalido.csv"
        with self.assertRaises(ValueError):
            self.control_csv.cargar_datos(ruta_archivo)
    def test_4_campos_mal_formato(self):
        """Archivo con campos que no cumplen formato.
            En este caso supondremos que hay una línea así:“123456a,Lulú López,1040,Cálculo”
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV/campoInvalido.csv"
        with self.assertRaises(ValueError):
            self.control_csv.cargar_datos(ruta_archivo)

    def test_5_archivo_lineas_duplicadas(self):
        """Archivo con líneas duplicadas.
            En este caso supondremos que hay unas líneas así:
            “1234567,Lulú López,1060,Administración
            1234567,Lulú López,1060,Administración”
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV/lineasDuplicadas.csv"
        resultado = self.control_csv.cargar_datos(ruta_archivo)
        self.assertEqual(len(resultado), 5)  # La línea duplicada aparece 2 veces
    def test_6_datos_nulos(self):
        """Archivo con datos nulos.
            En este caso supondremos que hay unas lineas asi: “1234567,,1040,Cálculo
            9876534,Pepito Pérez,1040,Cálculo
            4567766,Calvin Clein,1050,Física I
            1234567,Lulú López,1060,Administración
            4567766,Calvin Clein,,Espíritu Empresarial”
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV/camposNulos.csv"
        with self.assertRaises(Exception):
            self.control_csv.cargar_datos(ruta_archivo)

class TestCalcularTotalMaterias(unittest.TestCase):
    """Test para la clase Estudiante"""

    def setUp(self):
        self.control_csv = ControlArchivoCSV()

    def test_0_calcular_total_materias(self):
        """Test para calcular el total de materias inscritas por cada estudiante."""

        ruta = "archivosCSV/valido.csv"
        inscripciones = self.control_csv.cargar_datos(ruta)
        controlador = ControlProcesoInscripcion(inscripciones)
        resultado = controlador.calcular_total_materias()

        # Validaciones basadas en los datos del CSV
        self.assertEqual(resultado["1234567"]['total'], 2)
        self.assertEqual(resultado["9876534"]['total'], 1)
        self.assertEqual(resultado["4567766"]['total'], 2)

    def test_1_calcular_total_materias_con_cedula_diferente(self):
        """Calcular el total de materias para estudiantes con el mismo nombre y cédula diferente."""

        ruta_archivo = "archivosCSV/nombresIguales.csv"
        # Cargar los datos usando el método cargar_datos
        inscripciones = self.control_csv.cargar_datos(ruta_archivo)
        control_proceso = ControlProcesoInscripcion(inscripciones)
        resultado = control_proceso.calcular_total_materias()

        # Verificar que se cuenten correctamente las materias basadas en cédula
        self.assertEqual(resultado["1234567"]['total'], 2)
        self.assertEqual(resultado["9876534"]['total'], 1)
        self.assertEqual(resultado["4567766"]['total'], 2)
        self.assertEqual(resultado["9876534"]['total'], 1)

    def test_2_calcular_lista_vacia(self):
        """Calcular el total de materias con una lista vacía, es decir, no hay inscripciones."""
        ruta_archivo = "archivosCSV/vacio.csv"

        inscripciones = self.control_csv.cargar_datos(ruta_archivo)
        control_proceso = ControlProcesoInscripcion(inscripciones)
        resultado = control_proceso.calcular_total_materias()

        # Verificar los resultados esperados
        self.assertEqual(resultado, {})

    def test_3_calcular_datos_nulos(self):
        """Probar carga de datos con campos vacíos (nulos)."""
        ruta_archivo = "archivosCSV/camposNulos.csv"

        with self.assertRaises(ValueError):
            self.control_csv.cargar_datos(ruta_archivo)

    def test_4_calcular_linea_duplicada(self):
        """Calcular el total de materias con una lista vacía, es decir, no hay inscripciones."""
        ruta_archivo = "archivosCSV/lineasDuplicadas.csv"

        inscripciones = self.control_csv.cargar_datos(ruta_archivo)
        control_proceso = ControlProcesoInscripcion(inscripciones)
        resultado = control_proceso.calcular_total_materias()

        # Verificar los resultados esperados
        self.assertEqual(resultado["1234567"]['total'], 2)
        self.assertEqual(resultado["9876534"]['total'], 1)
        self.assertEqual(resultado["4567766"]['total'], 2)
if __name__ == '__main__':
    unittest.main()
