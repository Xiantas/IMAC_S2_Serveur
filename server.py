# -*- coding: utf-8 -*-

import os

from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS

import sqlite3

data_path = "database.db"

connection = sqlite3.connect(data_path)
a = 0

if not os.path.exists(data_path):
    with open("schema.sql") as f:
        connection.executescript(f.read())
    connection.commit()

app = Flask(__name__)
CORS(app)

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/order.html")
def order():
    return render_template("order.html")

@app.route("/order")
def parts_list():
    return jsonify({"list": ["pain", "salade", "viande", "tomate"]})

@app.route("/orders.html")
def orders():
    return "Non"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    print("Commiting database changes...")
    connection.commit()
    print("Saving database...")
    connection.close()
    print("Server shutdown")
