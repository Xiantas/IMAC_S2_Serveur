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
    
    def update_stocks(self,tab_ingredient_commande):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        
        for (const part of tab_ingredient_commande) 
        {
            cursor.execute("UPDATE stocks SET quantite=quantite-1 WHERE id_ingredient=part[0];")
        }

        connection.commit()
        connection.close()
        return 
   

    def get_ingredients(self):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT id_ingredient, nom_ingredient FROM stocks;")
        res = res.fetchall()
        connection.close()
        print("les ingrés :", res)
        return res

    #TODO
    def new_order(self, choix_ingredients,id_client):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        #order_array = [id_commande for ingre in choix_ingredients]
        #b = ", ".join(choix_ingredients)
        #a = ", ".join(order_array)
        id_order=cursor.execute("SELECT MAX(id_order) FROM orders")+1
        cursor.execute(f"INSERT INTO orders (id_order,id_client);")
        for (const part of choix_ingredients) 
        {
            cursor.execute(f"INSERT INTO orderparts (id_order,part);")
        }
        
        #res = cursor.execute(f"INSERT INTO orders ({a}) VALUES ({b});")
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
