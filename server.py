# -*- coding: utf-8 -*-

import database_interface

from flask import Flask,request,send_file,render_template,jsonify,abort
from flask_cors import CORS

import sqlite3

data_path = "database.db"
database_structure = "schema.sql"

database = database_interface.Database(data_path, database_structure, "")

app = Flask(__name__)
CORS(app)

@app.route("/index.html")
def index():
    print(jsonify(True))
    return render_template("index.html")

@app.route("/order.html", methods=['GET', 'POST'])
def order():
    if request.method == "POST":
        session = request.json
        if "email" not in session or "pw" not in session:
            return "{}"
        choix_ingredients = session["order"]
        compte_mail = session["email"]
        compte_pw = session["pw"]
        client_id = database.authentify(compte_mail, compte_pw)
        if client_id is not None:
            database.new_order(choix_ingredients, client_id)
            database.update_stocks(choix_ingredients)

        return "{}"
    return send_file("templates/order.html")

@app.route("/ingres")
def route_ingres():
    return jsonify(database.get_ingredients())

@app.route("/ingres_available")
def route_ingres_available():
    return jsonify(database.get_available_ingredients())

@app.route("/orderSummary.html")
def orderSummary():
    return send_file("templates/orderSummary.html")

@app.route("/orders.html")
def orders():
    return send_file("templates/orders.html")

@app.route("/orders", methods = ["GET", "DELETE"])
def ordersList():
    if request.method == "GET": #récupéré par orders.html
        order_list = database.get_orders()#c'est une liste de tuples avec id_order id_client TIMESTAMP id_ingredient
        return jsonify({"list": order_list})
    
    database.delete_orders(request.json)

    return "{}"

@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session = request.json
        if not ("email" in session and "pw" in session):
            return jsonify(False)
        email = session["email"]
        password = session["pw"]
        res=database.authentify(email,password)
        if res is not None:
            return jsonify(True)
        return jsonify(False)
    return send_file("templates/login.html")

@app.route("/register.html", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form.get("name")#si j'ai bien compris il faut la même chaine de caractère pour que le serveur reconnaisse la bonne ligne du form
        email = request.form.get("email")
        password = request.form.get("password")
        address = request.form.get("address")
        database.register(name,email,password,address)
        return send_file("templates/login.html")

    return send_file("templates/register.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    print("Server shutdown")
