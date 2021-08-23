from helper.generic import createResponse
from flask import jsonify
from model.User import User

def list():
    data = User().list()
    if len(data) > 0:
        response = createResponse(True, 200, "Data berhasil ditemukan", data)
    else:
        response = createResponse(False, 404, "Data tidak ditemukan")

    return jsonify(response), response["status_code"]
    

def store(data):
    user = User()
    stored = user.store(data)
    
    if stored:
        response = createResponse(True, 200, "User berhasil ditambahkan")
    else:
        response = createResponse(False, 500, "User gagal ditambahkan, silahkan coba lagi")

    return jsonify(response), response["status_code"]


def update(data, id):
    user = User()
    updated = user.update(data, id)
    
    if updated:
        response = createResponse(True, 200, "User berhasil diperbaharui")
    else:
        response = createResponse(False, 500, "User gagal diperbaharui, silahkan coba lagi")

    return jsonify(response), response["status_code"]


def destroy(id):
    user = User()
    deleted = user.destroy(id)
    
    if deleted:
        response = createResponse(True, 200, "User berhasil dihapus")
    else:
        response = createResponse(False, 500, "User gagal dihapus, silahkan coba lagi")

    return jsonify(response), response["status_code"]