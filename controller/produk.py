from helper.generic import createResponse
from flask import jsonify
from model.Produk import Produk

def list():
    data = Produk().list()
    if len(data) > 0:
        response = createResponse(True, 200, "Data berhasil ditemukan", data)
    else:
        response = createResponse(False, 404, "Data tidak ditemukan")

    return jsonify(response), response["status_code"]
    

def store(data):
    prod = Produk()
    stored = prod.store(data)
    
    if stored:
        response = createResponse(True, 200, "Produk berhasil ditambahkan")
    else:
        response = createResponse(False, 500, "Produk gagal ditambahkan, silahkan coba lagi")

    return jsonify(response), response["status_code"]


def update(data, id):
    prod = Produk()
    updated = prod.update(data, id)
    
    if updated:
        response = createResponse(True, 200, "Produk berhasil diperbaharui")
    else:
        response = createResponse(False, 500, "Produk gagal diperbaharui, silahkan coba lagi")

    return jsonify(response), response["status_code"]


def destroy(id):
    prod = Produk()
    deleted = prod.destroy(id)
    
    if deleted:
        response = createResponse(True, 200, "Produk berhasil dihapus")
    else:
        response = createResponse(False, 500, "Produk gagal dihapus, silahkan coba lagi")

    return jsonify(response), response["status_code"]