from flask import Flask, render_template, jsonify, redirect
import csv
import io

database = []

with io.open("files/database.csv", "r", encoding="utf-8") as archivo:
  reader = csv.reader(archivo)

  for line in reader:
    database.append({
      "id": int(line[0]),
      "name": line[1],
      "price": line[2],
      "currency": line[3],
      "detail": line[4],
      "ingredients": line[5],
      "picture": line[6],
      "category": line[7]
    })

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
  return render_template("index.html", products=database)

@app.route("/product/<int:id>")
def single_product(id):
  for product in database:
    if product["id"] == id:
      return render_template("single_product.html", product=product)

  return redirect("/")

@app.route("/products")
def products():
  return jsonify(database)