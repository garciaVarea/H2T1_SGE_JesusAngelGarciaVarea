import mysql.connector
from mysql.connector import Error

class EncuestaModelo:
    def __init__(self):
        self.conexion = self.conectar()

    def conectar(self):
        """Establece la conexión a la base de datos."""
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='curso',
                database='encuestas'
            )
            if conexion.is_connected():
                print("Conexión exitosa a la base de datos")
                return conexion
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos si está activa."""
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")

    """CREATE"""

    def crear_encuesta(self, datos):
        """Inserta un nuevo registro en la tabla ENCUESTA."""
        try:
            cursor = self.conexion.cursor()
            sql = """
            INSERT INTO ENCUESTA (idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana,
                                  BebidasDestiladasSemana, VinosSemana, PerdidasControl,
                                  DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, datos)
            self.conexion.commit()
            print("Registro insertado exitosamente")
        except Error as e:
            print(f"Error al insertar registro: {e}")
            raise e

    """READ"""
    def leer_encuestas(self):
        """Lee todos los registros de la tabla ENCUESTA."""
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM ENCUESTA")
            resultados = cursor.fetchall()
            return resultados
        except Error as e:
            print(f"Error al leer registros: {e}")
            return []

    """UPDATE"""
    def actualizar_encuesta(self, idEncuesta, campo, nuevo_valor):
        """Actualiza un campo específico de un registro en la tabla ENCUESTA."""
        try:
            cursor = self.conexion.cursor()
            sql = f"UPDATE ENCUESTA SET {campo} = %s WHERE idEncuesta = %s"
            cursor.execute(sql, (nuevo_valor, idEncuesta))
            self.conexion.commit()
            print("Registro actualizado exitosamente")
        except Error as e:
            print(f"Error al actualizar registro: {e}")

    """DELETE"""
    def eliminar_encuesta(self, idEncuesta):
        """Elimina un registro de la tabla ENCUESTA basado en su idEncuesta."""
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM ENCUESTA WHERE idEncuesta = %s"
            cursor.execute(sql, (idEncuesta,))
            self.conexion.commit()
            print("Registro eliminado exitosamente")
        except Error as e:
            print(f"Error al eliminar registro: {e}")

    """FILTROS"""
    def consultar_encuestas(self, orden=None, filtro=None):
        """Consulta encuestas con ordenación y filtros opcionales."""
        try:
            cursor = self.conexion.cursor()
            sql = "SELECT * FROM ENCUESTA"
            if filtro:
                sql += f" WHERE {filtro}"
            if orden:
                sql += f" ORDER BY {orden}"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as e:
            print(f"Error al consultar registros: {e}")
            return []