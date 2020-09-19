from app.model.sidang import Sidangs
from app import response,db
from flask import request,jsonify
from app.controllers import prodiController
from app import db
from flask_jwt_extended import *

import datetime
from app import mail
from flask_mail import Message
from flask import render_template

def store():
    try:
        tgl_daftar = request.json['tgl_daftar']
        npm = request.json['npm']
        nama_mhs = request.json['nama_mhs']
        jml_sks = request.json['jml_sks']
        prodi_id = request.json['prodi_id']
        email = request.json['email']

        sidang = Sidangs(prodi_id=prodi_id, tgl_daftar=tgl_daftar, npm=npm, nama_mhs=nama_mhs, jml_sks=jml_sks, email=email)
        db.session.add(sidang)
        db.session.commit()

        msg = Message(f"Hello, {nama_mhs} Welcome to Sistem Pendaftaran Sidang Online",
                      sender="agungwe2101@mail.com")
        msg.add_recipient(email)
        message_value = f"INFORMASI!!! Pendaftaran Sidang Online atas nama: {nama_mhs} dengan NPM: {npm} telah pihak Kampus terima. Terima kasih."
        msg.html = render_template('index.html',message_key=message_value)

        mail.send(msg)
        
        return response.ok('', 'Successfully Create Daftar Sidang !')
    except Exception as e:
        print(e)

@jwt_required
def index():
    try:
        id = request.args.get('prodi_id')
        sidang = Sidangs.query.filter_by(prodi_id = id).all()
        data = transform(sidang)
        return response.ok(data,"Data Daftar Sidang Ditemukan!")
    except Exception as e:
        print(e)

@jwt_required
def update(id):
    try:
        tgl_daftar = request.json['tgl_daftar']
        npm = request.json['npm']
        nama_mhs = request.json['nama_mhs']
        jml_sks = request.json['jml_sks']
        email = request.json['email']
        prodi_id = request.json['prodi_id']

        sidang = Sidangs.query.filter_by(id = id).first()
        sidang.tgl_daftar = tgl_daftar
        sidang.npm = npm
        sidang.nama_mhs = nama_mhs
        sidang.jml_sks = jml_sks
        sidang.email = email
        sidang.prodi_id = prodi_id
        db.session.commit()
        return response.ok('', 'Successfully update Daftar Sidang !')
    except Exception as e:
        print(e)

def show(id):
    try:
        sidang = Sidangs.query.filter_by(id=id).first()
        if not sidang:
            return response.badRequest([], 'Empty....')
        data = singleTransform(sidang)
        return response.ok(data,"Data Daftar Sidang Ditemukan!")
    except Exception as e:
        print(e)

def delete(id):
    try:
        sidang = Sidangs.query.filter_by(id = id).first()
        if not sidang:
            return response.badRequest([], 'Empty....')
        db.session.delete(sidang)
        db.session.commit()
        return response.ok('', 'Successfully delete Daftar Sidang !')
    except Exception as e:
        print(e)


def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array


def singleTransform(values):
    print(values.prodis.id)
    print(values.prodis.nama_prodi)
    print(values.prodis.fakultas)
    data = {
        'id' : values.id,
        'user_id': values.prodi_id,
        'tgl_daftar': values.tgl_daftar,
        'npm': values.npm,
        'nama_mhs': values.nama_mhs,
        'jml_sks': values.jml_sks,
        'email': values.email,
        'created_at': values.created_at,
        'updated_at': values.updated_at,
        'prodi': prodiController.singleTransform(values.prodis, withSidang=False)
    }

    return data