"""importando librerias necesarias para el test"""
import unittest
from controlArchivoCSV import ControlArchivoCSV
from controlProcesoInscripciones import ControlProcesoInscripcion

class TestInscripciones(unittest.TestCase):
    """Test para la clase Estudiante"""

    def setUp(self):
        self.control_archivo = ControlArchivoCSV()
        self.control_proceso = ControlProcesoInscripcion(inscripciones=[])

    def test_calcular_total_inscripciones_desde_csv(self):
        """Test para calcular el total de materias inscritas por cada estudiante."""

        ruta = "archivosCSV/valido.csv"
        controlador_csv = ControlArchivoCSV()
        inscripciones = controlador_csv.cargar_datos(ruta)

        controlador = ControlProcesoInscripcion(inscripciones)
        resultado = controlador.calcular_total_inscripciones()

        # Validaciones basadas en los datos del CSV
        self.assertEqual(resultado["Lulú López"], 2)
        self.assertEqual(resultado["Pepito Pérez"], 1)
        self.assertEqual(resultado["Calvin Clein"], 2)

    def test_calcular_total_materias_con_cedula_diferente(self):
        """Calcular el total de materias para estudiantes con el mismo nombre y cédula diferente."""

        # Crear un archivo CSV en memoria (como si fuera un archivo físico)
        ruta_archivo = "archivosCSV/nombresIguales.csv"
        # Cargar los datos usando el método cargar_datos
        inscripciones = self.control_archivo.cargar_datos(ruta_archivo)

        # Contador para las materias de cada estudiante, ahora usando cédula
        contador = {}

        for ins in inscripciones:
            estudiante = ins.getestudiante()
            cedula = estudiante.getcedula()
            contador[cedula] = contador.get(cedula, 0) + 1

        # Verificar que se cuenten correctamente las materias basadas en cédula
        self.assertEqual(contador["1234567"], 2)  # Lulú López con cédula 1234567
        self.assertEqual(contador["9876534"], 1)  # Pepito Pérez con cédula 9876534
        self.assertEqual(contador["4567766"], 2)  # Calvin Clein con cédula 4567766
        self.assertEqual(contador["9878989"], 1)  # Otro Pepito Pérez con cédula 9878989

class TestControlArchivoCSV(unittest.TestCase):
    """Test para la clase ControlArchivoCSV que maneja la carga de datos desde un archivo CSV."""

    def setUp(self):
        self.control = ControlArchivoCSV()

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
            self.control.cargar_datos(ruta_archivo)
    def test_2_archivo_vacio(self):
        """Test Archivo CSV vacío, es decir, el archivo existe pero no contiene ningún dato."""
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV/vacio.csv"
        resultado = self.control.cargar_datos(ruta_archivo)
        self.assertEqual(resultado, [])
    def test_3_archivo_datos_incompletos(self):
        """Test de archivo con datos incompletos donde falta algún campo en la línea CSV.
            En este caso supondremos que hay una línea así: “9876534,Pepito Pérez,1040 ”
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV/campoInvalido.csv"
        with self.assertRaises(ValueError):
            self.control.cargar_datos(ruta_archivo)
    def test_4_campos_mal_formato(self):
        """Archivo con campos que no cumplen formato.
            En este caso supondremos que hay una línea así:“123456a,Lulú López,1040,Cálculo”
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV/campoInvalido.csv"
        with self.assertRaises(ValueError):
            self.control.cargar_datos(ruta_archivo)

    def test_5_archivo_lineas_duplicadas(self):
        """Archivo con líneas duplicadas. 
            En este caso supondremos que hay unas líneas así:
            “1234567,Lulú López,1060,Administración 
            1234567,Lulú López,1060,Administración”
        """
        #Ruta del archivo de prueba
        ruta_archivo = "archivosCSV/lineasDuplicadas.csv"
        resultado = self.control.cargar_datos(ruta_archivo)
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
            self.control.cargar_datos(ruta_archivo)

if __name__ == '__main__':
    unittest.main()
