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
        database.new_order(choix_ingredients,1)# met à jour oders et orderpart dans la bdd
        database.update_stocks(choix_ingredients)#met à jour stocks 

        return "{}"
    return render_template("order.html")

@app.route("/ingres")
def parts_list():
    return jsonify({"list": database.get_ingredients()})# récupéré apr order.thml

@app.route("/ingresetprix")#utilisé dans order
def parts_list2():
    return jsonify({"list": database.get_ingredients_et_prix()})# récupéré apr order.thml

@app.route("/orderSummary.html")
def orderSummary():
    return render_template("orderSummary.html")

@app.route("/orders.html")
def orders():
    return render_template("orders.html")

@app.route("/orders", methods = ["GET", "POST"])
def ordersList():
    if request.method == "GET": #récupéré par orders.html
        order_list = database.get_orders()#c'est une liste de tuples avec id_order id_client TIMESTAMP id_ingredient
        return jsonify({"list": order_list})
    
    database.delete_orders(request.json)

    return "{}"

@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("adresse_mail")
        password = request.form.get("password")
        res=database.login(email,password)
        if len(res)==0:
            return render_template("login.html")
        return render_template("order.html")
    return render_template("login.html")

@app.route("/register.html", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form.get("name")#si j'ai bien compris il faut la même chaine de caractère pour que le serveur reconnaisse la bonne ligne du form
        email = request.form.get("email")
        password = request.form.get("password")
        address = request.form.get("address")
        database.register(name,email,password,address)
        return render_template("order.html")

    return render_template("register.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    print("Server shutdown")
