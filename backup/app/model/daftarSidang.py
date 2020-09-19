from app import db
from datetime import datetime
from app.model.user import Users
from app.model.prodi import Prodis


class daftarSidangs(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nim = db.Column(db.String(10), unique=True, nullable=False)
    nama_mahasiswa = db.Column(db.String(100), nullable=False)
    tgl_daftar = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    prodi_id = db.Column(db.BigInteger, db.ForeignKey(Prodis.id))
    prodis = db.relationship("Prodis", backref="prodi_id")

    def __repr__(self):
        return '<DaftarSidang {}>'.format(self.nama_mahasiswa)