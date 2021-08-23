from helper.generic import createResponse
from flask import jsonify
from helper.generic import createResponse
from model.alamat.Provinsi import Provinsi
from model.alamat.Kabupaten import Kabupaten
from model.alamat.Kecamatan import Kecamatan
from model.alamat.Kelurahan import Kelurahan

def listProvinsi():
    data = Provinsi().list()
    if len(data) > 0:
        response = createResponse(True, 200, "Data berhasil ditemukan", data)
    else:
        response = createResponse(False, 404, "Data tidak ditemukan")
        
    return jsonify(response), response["status_code"]
    
def listKabupaten(prov_id):
    data = Kabupaten().list(prov_id)
    if len(data) > 0:
        response = createResponse(True, 200, "Data berhasil ditemukan", data)
    else:
        response = createResponse(False, 404, "Data tidak ditemukan")
        
    return jsonify(response), response["status_code"]
    
def listKecamatan(kab_id):
    data = Kecamatan().list(kab_id)
    if len(data) > 0:
        response = createResponse(True, 200, "Data berhasil ditemukan", data)
    else:
        response = createResponse(False, 404, "Data tidak ditemukan")
        
    return jsonify(response), response["status_code"]
    
def listKelurahan(kec_id):
    data = Kelurahan().list(kec_id)
    if len(data) > 0:
        response = createResponse(True, 200, "Data berhasil ditemukan", data)
    else:
        response = createResponse(False, 404, "Data tidak ditemukan")
        
    return jsonify(response), response["status_code"]