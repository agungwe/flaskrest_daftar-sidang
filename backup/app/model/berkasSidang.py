from app import db
from datetime import datetime
from app.model.daftarSidang import daftarSidangs


class berkasSidangs(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    file_name = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    daftarsidang_id = db.Column(db.BigInteger, db.ForeignKey(daftarSidangs.id))
    daftarsidangs = db.relationship("daftarSidangs", backref="daftarsidang_id")


    def __repr__(self):
        return '<DaftarSidang {}>'.format(self.nama_mahasiswa)