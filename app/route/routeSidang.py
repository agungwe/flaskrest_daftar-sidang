from app import app
from app.controllers import sidangController, sidangFileController
from flask import request


@app.route('/daftar-sidang', methods=['POST','GET'])
def sidang():
    if request.method == 'POST':
        return sidangController.store()
    elif request.method == 'GET':
        return sidangController.index()


@app.route('/daftar-sidang/<id>', methods=['PUT','GET','DELETE'])
def sidangDetail(id):
    if request.method == 'GET':
        return sidangController.show(id)
    elif request.method == 'PUT':
        return sidangController.update(id)
    elif request.method == 'DELETE':
        return sidangController.delete(id)



@app.route('/sidang-files/<id>', methods=['POST','GET'])
def sidangFiles(id):
    if request.method == 'POST':
        return sidangFileController.store(id)
    if request.method == 'GET':
        return sidangFileController.index(id)