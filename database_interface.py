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
        
        for part in tab_ingredient_commande:
            cursor.execute(f"UPDATE stocks SET quantite=quantite-1 WHERE id_ingredient={part[0]};")
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
        cursor.execute(f"INSERT INTO orders (NULL,{id_client}, NULL);")
        id_order = cursor.lastrowid
        for part in choix_ingredients :
            cursor.execute(f"INSERT INTO orderparts ({id_order},{part});")
        
        #res = cursor.execute(f"INSERT INTO orders ({a}) VALUES ({b});")
        connection.commit()
        connection.close()


    #TODO
    def get_orders(self): #utilisé dans /orders 
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT * FROM orders JOIN orderparts ON order.id_order=orderparts.id_order ORDERBY id_client;")#ca nous donne id_order id_client TIMESTAMP id_ingredient, liste de tupes à 4 éléments 
        res = res.fetchall()
        #def ingres_to_str(tup):
            #ingres = ", ".join([ingredients[i] for (i, b) in enumerate(tup[2:]) if b])
            #return (tup[0], tup[1], ingres)
        #res = list(map(ingres_to_str, res))
        return res 

    #TODO
    def delete_orders(self, ids):
        connection = sqlite3.connect(data_path)
        cursor = connection.cursor()
        ids = ", ".join(map(lambda idt : str(idt), ids))
        cursor.execute(f"DELETE FROM orders WHERE nb_commande IN ({ids});")
        connection.commit()
