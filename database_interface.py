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
        res = cursor.execute("SELECT id_ingredient, nom_ingredient FROM stocks WHERE quantite>0;")
        res = res.fetchall()
        connection.close()
        return res

    def get_ingredients_et_prix(self):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT id_ingredient, nom_ingredient,prix FROM stocks WHERE quantite>0 ;")
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

        liste_id="("
        for part in choix_ingredients :
            liste_id+=part
            liste_id+=","
        liste_id=liste_id[:-1]
        liste_id+=")"
        liste_prix=cursor.execute(f"SELECT prix FROM id_ingredient WHERE id_ingredient IN liste_id ;")
        prix_total=0
        for part in liste_prix :
            prix_total+=part

        cursor.execute(f"INSERT INTO orders (id_client,prix_total) VALUES ({id_client},{prix_total});")
        id_order = cursor.lastrowid
        for part in choix_ingredients :
            cursor.execute(f"INSERT INTO orderparts VALUES ({id_order},{part});")

        connection.commit()
        connection.close()


    def get_orders(self): #utilisé dans /orders 
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT orders.id_order, nom_client, created, id_ingredient, adresse FROM orders JOIN orderparts ON orders.id_order=orderparts.id_order JOIN clients ON orders.id_client=clients.id_client ORDER BY orders.id_order;")#ca nous donne id_order id_client TIMESTAMP id_ingredient, liste de tupes à 4 éléments 
        res = res.fetchall() 
        
        return res 

    #TODO
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

    def login(self,email,password):
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        
        res = cursor.execute(f"SELECT id_client FROM clients WHERE adresse_mail='{email}' AND mdp='{password}';")
        res = res.fetchall()
        connection.close()
        return res
        
