import os
import sqlite3

class Database:
    def __init__(self, database_path, schema_path, data_folder):
        self.__path = database_path
        if not os.path.exists(database_path):
            self.reload(schema_path, data_folder)


    def reload(self, schema_path, data_folder):
        connection = sqlite3.connect(self.__path)

        with open(schema_path) as f:
            connection.executescript(f.read())

        self.__load_data(connection, data_folder)
        connection.commit()

        connection.close()


    def __load_data(self, connection, data_folder):
        pass #TODO parser


    def get_ingredients(self):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT id_ingredient, nom_ingredient FROM stocks;")
        res = res.fetchall()
        connection.close()
        noms = list(map(lambda t : t[0], res))
        print("les ingrés :", res)
        return res
