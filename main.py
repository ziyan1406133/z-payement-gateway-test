from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

# print(os.environ["DATABASE_URL"])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hgfcicgedydrjq:7ab96ad474cdb4e78fe0c70d0ab5fe00134ebac928500c4e0c65346d3d2622af@ec2-18-235-45-217.compute-1.amazonaws.com:5432/ded6sc2rb2b630"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# print(app.config['SQLALCHEMY_DATABASE_URI'])

from controller import transcations, alamat, produk, user
from model.alamat import Provinsi, Kabupaten, Kecamatan, Kelurahan
from model import Produk, User, Order

@app.route("/", methods=["GET"])
def index():
    return transcations.homepage(request.args)

###

#
@app.route("/list-provinsi", methods=["GET"])
def provinsi():
    return alamat.listProvinsi()

@app.route("/list-kabupaten/<int:prov_id>", methods=["GET"])
def kabupaten(prov_id):
    return alamat.listKabupaten(prov_id)

@app.route("/list-kecamatan/<int:kab_id>", methods=["GET"])
def kecamatan(kab_id):
    return alamat.listKecamatan(kab_id)

@app.route("/list-kelurahan/<int:kec_id>", methods=["GET"])
def kelurahan(kec_id):
    return alamat.listKelurahan(kec_id)

#
@app.route("/produk", methods=["GET", "POST"])
def get_post_produk():
    if request.method == 'GET':
        return produk.list()
    elif request.method == 'POST':
        return produk.store(request.json)
        
@app.route("/produk/<int:produk_id>", methods=["PUT", "DELETE"])
def put_delete_produk(produk_id):
    if request.method == 'PUT':
        return produk.update(request.json, produk_id)
    elif request.method == 'DELETE':
        return produk.destroy(produk_id)


#
@app.route("/user", methods=["GET", "POST"])
def get_post_user():
    if request.method == 'GET':
        return user.list()
    elif request.method == 'POST':
        return user.store(request.json)
        
@app.route("/user/<int:user_id>", methods=["PUT", "DELETE"])
def put_delete_user(user_id):
    if request.method == 'PUT':
        return user.update(request.json, user_id)
    elif request.method == 'DELETE':
        return user.destroy(user_id)


###

@app.route("/scan-token", methods=["POST"])
def scanToken():
    return transcations.scanToken(request.json)

@app.route("/order-status", methods=["PUT"])
def updateStatusOrder():
    return transcations.updateStatusOrder(request.json)

@app.route("/list-order/<int:user_id>", methods=["GET"])
def listOrder(user_id):
    return transcations.listOrder(user_id)

if __name__ == "__main__":
    app.run();
    db.create_all()