from mysql.connector import connect, Error
from enum import Enum
import pandas as pd


class Conexion(Enum):
    HOST = "localhost"
    USER = "root"
    PASSWORD = "Ab@ntonio347"
    DATABASE = "Twitter"
    ARCHIVO = "datasets/bitcoin-tweets.csv"


class Mysqlconnect():
    def __init__(self, host, user, password, database):
        self._host = Conexion.HOST.value
        self._user = Conexion.USER.value
        self._password = Conexion.PASSWORD.value
        self._database = Conexion.DATABASE.value
        self.dbconexion = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, value):
        self._database = value

    def conectar(self):
        try:
            self.dbconexion = connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )

            print(
                f"Conexion abierta\nTipo de conexión: {type(self.dbconexion)}"
            )

        except Error as e:
            print(e)

    def desconectar(self):
        if self.dbconexion is not None:
            self.dbconexion.close()
            print("Se ha cerrado la conexión con la base de datos")


class Bitcoin(Mysqlconnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.cursor = None

    def insertar(self, value, archivo):
        self.conectar()

        try:
            self.cursor = self.dbconexion.cursor()
            twitter = pd.read_csv(archivo, delimiter=";")

            for _, row in twitter.iterrows():
                sql = "INSERT INTO Twitter_bitcoins (fecha, usuario, texto, likes) VALUES (%s, %s, %s, %s)"
                val = tuple(row)
                self.cursor.execute(sql, val)

            self.dbconexion.commit()
            self.cursor.close()
            self.desconectar()
            print("Inserción de datos exitosa")
            return True

        except Error as e:
            self.desconectar()
            print(f"Error al agregar datos: {e}")
            return False

    def leer_tweets(self):
        self.conectar()

        try:
            self.cursor = self.dbconexion.cursor()
            sql = "SELECT * FROM Twitter_bitcoins"

            tweets_df = pd.read_sql(sql, con=self.dbconexion)

            print(tweets_df)

        except Error as e:
            self.desconectar()
            print(f"Error al crear el data frame: {e}")
            return False

    def contar_filas(self):
        try:
            self.cursor = self.dbconexion.cursor()
            sql = "SELECT COUNT(*) FROM Twitter_Bitcoins"
            self.cursor.execute(sql)
            count = self.cursor.fetchone()[0]
            return count
        except Error as e:
            print(f"Error al contar filas: {e}")
            return None

    def top_likes(self, value):
        self.conectar()

        try:
            filas = self.contar_filas()
            if value <= filas:
                self.cursor = self.dbconexion.cursor()
                sql = f"SELECT * FROM Twitter_Bitcoins ORDER BY likes DESC LIMIT {value}"
                top_likes_df = pd.read_sql(sql, con=self.dbconexion)

                print(top_likes_df)

            else:
                print("La cantidad buscada es mayor a la cantidad de datos")

        except Error as e:
            self.desconectar()
            print(f"Error al retornar datos: {e}")
            return False



if __name__ == "__main__":
    db = Bitcoin(Conexion.HOST.value, Conexion.USER.value, Conexion.PASSWORD.value, Conexion.DATABASE.value)
    #db.insertar(1, Conexion.ARCHIVO.value)
    db.leer_tweets()
    db.top_likes(13)
