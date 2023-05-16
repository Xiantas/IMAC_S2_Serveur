# -*- coding: utf-8 -*-

import os

from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS

import sqlite3

data_path = "database.db"
database_structure = "schema.sql"

connection = None

if not os.path.exists(data_path):
    print("Creating database")
    connection = sqlite3.connect(data_path)

    with open(database_structure) as f:
        connection.executescript(f.read())
else:
    connection = sqlite3.connect(data_path)

def getIngredients():
    cursor = connection.cursor()
    res = cursor.execute("SELECT nom_ingredient FROM stocks;")
    res = res.fetchall()
    noms = list(map(lambda t : t[0], res))
    print(noms)
    return noms
ingredients = getIngredients()

connection.commit()
connection.close()

app = Flask(__name__)
CORS(app)

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/order.html", methods=['GET', 'POST'])
def order():
    if request.method == "POST":
        choix_ingredients = request.json
        connection = sqlite3.connect(data_path)
        cursor = connection.cursor()
        orderArray = [str(ingre in choix_ingredients) for ingre in ingredients]
        a = ", ".join(ingredients)
        b = ", ".join(orderArray)
        res = cursor.execute(f"INSERT INTO orders ({a}) VALUES ({b});")
        connection.commit()
        connection.close()
        return "{}"
    return render_template("order.html")

@app.route("/order")
def parts_list():
    return jsonify({"list": ingredients})

@app.route("/orderSummary.html")
def orderSummary():
    return render_template("orderSummary.html")

@app.route("/orders.html")
def orders():
    return render_template("orders.html")

@app.route("/orders", methods = ["GET", "POST"])
def ordersList():
    if request.method == "GET":
        connection = sqlite3.connect(data_path)
        cursor = connection.cursor()
        res = cursor.execute("SELECT * FROM orders;")
        res = res.fetchall()

        def ingres_to_str(tup):
            ingres = ", ".join([ingredients[i] for (i, b) in enumerate(tup[2:]) if b])
            return (tup[0], tup[1], ingres)
        res = list(map(ingres_to_str, res));

        print(res)
        connection.close()
        return jsonify({"list": res})

    connection = sqlite3.connect(data_path)
    cursor = connection.cursor()
    print(f"delete: {request.json}")
    ids = ", ".join(map(lambda idt : str(idt), request.json))
    cursor.execute(f"DELETE FROM orders WHERE nb_commande IN ({ids});")
    connection.commit()
    connection.close()

    return "{}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    print("Server shutdown")
