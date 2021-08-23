import json
from flask import jsonify
from model.alamat.Provinsi import Provinsi
from model.alamat.Kabupaten import Kabupaten
from model.alamat.Kecamatan import Kecamatan
from model.alamat.Kelurahan import Kelurahan
from model.Produk import Produk
from model.Order import Order
from model.User import User
from helper.generic import *

from datetime import datetime
import midtransclient
import os
import requests
import json

def scanToken(data):
    # return jsonify(data)

    snap = midtransclient.Snap(
        is_production=False,
        server_key="SB-Mid-server-FVAXT1qbO3l8I5y9ZqM4kNYE"
    )

    item_details = list()
    gross_amount = 0
    for item in data["item_details"]:
        produk = Produk().query.get(item["id"])
        subtotal = produk.harga * item["quantity"]
        gross_amount += subtotal
        item_details.append({
            "id": produk.id,
            "price" : produk.harga,
            "quantity" : item["quantity"],
            "name": produk.nama
        })

    user = User().query.get(data["buyer_id"])
    # provinsi = Provinsi().query.get(data["shipping_address"]["provinsi_id"]).nama
    kabupaten = Kabupaten().query.get(data["shipping_address"]["kabupaten_id"]).nama
    # kecamatan = Kecamatan().query.get(data["shipping_address"]["kecamatan_id"]).nama
    # alamat_lengkap = "{}, {}, {}, {}".format(data["shipping_address"]["address"], kecamatan, kabupaten, provinsi)

    random_number = generateRandomNumber(5)
    now = datetime.now()
    expire_start = now.strftime("%Y-%m-%d %H:%M:%S +0700")
    order_id = "CustOrder-{}".format(random_number)

    param = {
        "transaction_details": {
            "order_id": order_id,
            "gross_amount": gross_amount
        },
        "credit_card": {
            "secure": True
        },
        "item_details": item_details,
        "customer_details": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "phone": user.phone_no,
                "shipping_address": {
                    "first_name": data["shipping_address"]["first_name"],
                    "last_name": data["shipping_address"]["last_name"],
                    "email": data["shipping_address"]["email"],
                    "phone": data["shipping_address"]["phone"],
                    "address": data["shipping_address"]["address"],
                    "city": kabupaten,
                    "postal_code": data["shipping_address"]["postal_code"],
                    "country_code": "IDN"
            }
        },
        "expiry": {
            "start_time": expire_start,
            "unit": "hours",
            "duration": 24
        },
    }

    # stored_response = storeOrder(order_id, user.id)
    # return jsonify(stored_response)
    try:
        data = snap.create_transaction(param)
        data["order_id"] = order_id
        data["buyer_id"] = user.id

        create_new = Order().update(data)
        if create_new:
            response = createResponse(True, 200, "Status Order Berhasil Diperbaharui")
        else:
            response = createResponse(True, 200, "Status Order Gagal Diperbaharui", data)

        response = createResponse(True, 200, "Transaksi sedang diproses", data)
    except Exception as e:
        response = createResponse(False, 500, "Terjadi kesalahan", str(e))

    return jsonify(response), response["status_code"]


def updateStatusOrder(data):
    url = "https://api.sandbox.midtrans.com/v2/{}/status".format(data["order_id"])
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Basic U0ItTWlkLXNlcnZlci1GVkFYVDFxYk8zbDhJNXk5WnFNNGtOWUU6'
    }
    
    payload = requests.request("GET", url, headers=headers)
    payload = payload.text.encode('utf8')
    payload = json.loads(payload)

    if payload["status_code"] == "407" or payload["status_code"] == "200":

        payload["buyer_id"] = data["buyer_id"]
        updated = Order().update(payload)
        if updated:
            response = createResponse(True, 200, "Status Order Berhasil Diperbaharui")
        else:
            response = createResponse(True, 200, "Status Order Gagal Diperbaharui", payload)
    else:
        response = createResponse(False, payload["status_code"], payload["status_message"], payload) 

    return response

def listOrder(user_id):
    data = Order().list(user_id)
    if len(data) > 0:
        response = createResponse(True, 200, "Data berhasil ditemukan", data)
    else:
        response = createResponse(False, 404, "Data tidak ditemukan")

    return jsonify(response), response["status_code"]


def homepage(args):
    data = args.copy()
    if "order_id" in args:
        order = Order().query.filter_by(order_id="CustOrder-32626").first()
        data["buyer_id"] = order.buyer_id

        update = updateStatusOrder(data)
        print(update)
        if update["success"]:
            return "Terima kasih telah berbelanja di sini. Transaksi telah diproses"
        else:
            return "Terjadi kesalahan ketika menyimpan data transaksi"

    else:
        return "Payment Gateway w/ Midtrans"