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

        connection.commit()
        connection.close()

    def update_stocks(self,tab_ingredient_commande):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        
        for part in tab_ingredient_commande:
            cursor.execute(f"UPDATE stocks SET quantite=quantite-1 WHERE id_produit={part[0]} AND quantite>0;")
        connection.commit()
        connection.close()
        return 
   

    def get_ingredients(self):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT id_produit, nom_produit, prix FROM stocks")
        res = res.fetchall()
        connection.close()
        return res

    def get_available_ingredients(self):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT id_produit, nom_produit, prix FROM stocks WHERE quantite>0;")
        res = res.fetchall()
        connection.close()
        return res

    def get_ingredients_et_prix(self):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT id_produit, nom_produit,prix FROM stocks WHERE quantite>0 ;")
        res = res.fetchall()
        connection.close()
        print("les ingrés :", res)
        return res


    def new_order(self, choix_ingredients,id_client):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        adresse=""
        password=""
        res = cursor.execute(f"SELECT id_client FROM clients WHERE adresse='{adresse}' AND mdp='{password}';")
        res = res.fetchall()

        id_list = ", ".join(map(lambda i : str(i[0]), res));
        liste_prix=cursor.execute(f"SELECT prix FROM stocks WHERE id_produit IN ({id_list});")
        prix_total=sum(liste_prix)

        cursor.execute(f"INSERT INTO orders (id_client,prix_total) VALUES ({id_client},{prix_total});")
        id_order = cursor.lastrowid
        for part in choix_ingredients :
            cursor.execute(f"INSERT INTO orderparts SELECT {id_order},id_produit FROM stocks WHERE id_produit={part};")

        connection.commit()
        connection.close()


    def get_orders(self):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT orders.id_order, nom_client, created, id_produit, adresse FROM orders JOIN orderparts ON orders.id_order=orderparts.id_order JOIN clients ON orders.id_client=clients.id_client ORDER BY orders.id_order;")
        res = res.fetchall() 
        
        return res 

    def delete_orders(self, ids):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        ids = ", ".join(map(lambda idt : str(idt), ids))
        cursor.execute(f"DELETE FROM orders WHERE id_order IN ({ids});")
        connection.commit()
        connection.close()

    def register(self,name,email,password,address):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO clients VALUES (NULL,'{name}','{email}','{password}','{address}');")
        print(cursor.execute(f"SELECT * FROM clients;").fetchall())
        connection.commit()
        connection.close()

    def authentify(self,email,password):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()

        res = cursor.execute(f"SELECT id_client FROM clients WHERE adresse_mail='{email}' AND mdp='{password}';")
        res = res.fetchall()
        connection.close()
        if len(res)>0:
            return res[0][0]
        return None
