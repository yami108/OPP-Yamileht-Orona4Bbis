import psycopg2
from psycopg2 import Error
from psycopg2.extras import RealDictCursor
from Controller.config import DB_config

class Database_connection:
    def __init__(self):
        self.config = DB_config

    def obtener_conexion(self):
        try:
            conexion = psycopg2.connect(**self.config)
            return conexion
        except Error as e:
            print(f"Error al conectar con PostgreSQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=()):
        conexion = self.obtener_conexion()
        if not conexion:
            return None

        # RealDictCursor permite obtener resultados como diccionarios (clave: valor)
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute(query, params)
            
            # Si la consulta devuelve datos (SELECT)
            if cursor.description:
                resultados = cursor.fetchall()
            else:
                conexion.commit()
                resultados = None
                
            return resultados
        except Error as e:
            print(f"Error en la consulta SQL: {e}")
            conexion.rollback()
            return None
        finally:
            cursor.close()
            conexion.close()