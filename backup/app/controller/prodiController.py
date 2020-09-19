from app.model.prodi import Prodis
from flask import request, jsonify
from app import response, db
#from app.controller import userController

def store():
    try:
        nama_prodi = request.json['kode_prodi']
        fakultas = request.json['fakultas']

        prodi = Prodis(nama_prodi=nama_prodi, fakultas=fakultas)
        db.session.add(prodi)
        db.session.commit()

        return response.ok('', 'Successfully Create Program Studi!')

    except Exception as e:
        print(e)


def index():
    try:
        id = request.args.get('id')
        prodi = Todos.query.filter_by(id=id).all()
        data = transform(prodi)
        return response.ok(data, "Data Program Studi ditemukan..")
    except Exception as e:
        print(e)


def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array


def singleTransform(values):
    # print(values.users.id)
    # print(values.users.email)
    data = {
        'id': values.id,
        'nama_prodi': values.nama_prodi,
        'fakultas': values.fakultas,
        'created_at': values.created_at,
        'updated_at': values.updated_at
    }

    return data



def update(id):
    try:
        inputProdi = request.json['nama_prodi']
        inputFak = request.json['fakultas']
        prodi = Prodis.query.filter_by(id=id).first()
        
        prodi.nama_prodi = inputProdi
        prodi.fakultas = inputFak
        db.session.commit()
        return response.ok('', 'Successfully Update Program Studi!')
    except Exception as e:
        print(e)


def show(id):
    try:
        prodi = Prodis.query.filter_by(id=id).first()
        if not prodi:
            return response.badRequest([], 'Empty....')

        data = singleTransform(prodi)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def delete(id):
    try:
        prodi = Todos.query.filter_by(id=id).first()
        if not prodi:
            return response.badRequest([], 'Empty....')

        db.session.delete(prodi)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        print(e)


