from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controller import transcations, alamat, produk, user
from model.alamat import Provinsi, Kabupaten, Kecamatan, Kelurahan
from model import Produk, User, Order

@app.route("/")
def index():
    return "Payment Gateway w/ Midtrans"

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


# @app.context_processor
# def inject_stage_and_region():
# 	return dict(MERCHANT_ID=os.environ["MERCHANT_ID"],
# 		CLIENT_KEY=os.environ["CLIENT_KEY"],
# 		SERVER_KEY=os.environ["SERVER_KEY"])

if __name__ == "__main__":
    app.run()
    db.create_all()