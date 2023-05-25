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
    
    def update_stocks(self,liste_ingredient_commande):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        cursor.execute("UPDATE stocks SET quantite=quantite-1 WHERE nom_ingredient=part;")
        connection.close()
        return 

    def get_ingredients(self):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT id_ingredient, nom_ingredient FROM stocks;")
        res = res.fetchall()
        connection.close()
        noms = list(map(lambda t : t[0], res))
        print("les ingrés :", res)
        return res

    #TODO
    def new_order(self, choix_ingredients):
        ingredients = database.get_ingredients()
        connection = sqlite3.connect(data_path)
        cursor = connection.cursor()
        order_array = [str(ingre in choix_ingredients) for ingre in ingredients]
        a = ", ".join(ingredients)
        b = ", ".join(order_array)
        res = cursor.execute(f"INSERT INTO orders ({a}) VALUES ({b});")
        connection.commit()
        connection.close()


    #TODO
    def get_orders(self):
        connection = sqlite3.connect(data_path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT * FROM orders;")
        res = res.fetchall()

        def ingres_to_str(tup):
            ingres = ", ".join([ingredients[i] for (i, b) in enumerate(tup[2:]) if b])
            return (tup[0], tup[1], ingres)
        res = list(map(ingres_to_str, res));

    #TODO
    def delete_orders(self, ids):
        connection = sqlite3.connect(data_path)
        cursor = connection.cursor()
        ids = ", ".join(map(lambda idt : str(idt), ids))
        cursor.execute(f"DELETE FROM orders WHERE nb_commande IN ({ids});")
        connection.commit()
