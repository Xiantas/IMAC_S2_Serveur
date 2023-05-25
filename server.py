# -*- coding: utf-8 -*-

import database_interface

from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS

import sqlite3

data_path = "database.db"
database_structure = "schema.sql"

database = database_interface.Database(data_path, database_structure, "")

app = Flask(__name__)
CORS(app)

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/order.html", methods=['GET', 'POST'])
def order():
    if request.method == "POST": #lancé depuis /order.html 
        choix_ingredients = request.json #récupère ce que j'ai envoyé avec le fetch
        database.new_order(choix_ingredients,"NULL")# met à jour oders et orderpart dans la bdd
        database.update_stocks(choix_ingredients)#met à jour stocks 

        return "{}"
    return render_template("order.html")

@app.route("/order")
def parts_list():
    return jsonify({"list": database.get_ingredients})# récupéré apr order.thml

@app.route("/orderSummary.html")
def orderSummary():
    return render_template("orderSummary.html")

@app.route("/orders.html")
def orders():
    return render_template("orders.html")

@app.route("/orders", methods = ["GET", "POST"])
def ordersList():
    if request.method == "GET":
        order_list = database.get_orders()

        print(res)
        connection.close()
        return jsonify({"list": res})

    connection.close()
    database.delete_orders(request.json)

    return "{}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    print("Server shutdown")
