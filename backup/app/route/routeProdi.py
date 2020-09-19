from app import app
from app.controller import prodiController
from flask import request

@app.route('/prodi', methods=['POST','GET'])
def todo():
    if request.method == 'POST':
        return prodiController.store()
    elif request.method == 'GET':
        return prodiController.index()


@app.route('/prodi/<id>', methods=['PUT', 'GET', 'DELETE'])
def todoDetail(id):
    if request.method == 'GET':
        return prodiController.show(id)
    elif request.method == 'PUT':
        return prodiController.update(id)
    elif request.method == 'DELETE':
        return prodiController.delete(id)