from app import db
from datetime import datetime
#from app.model.daftarSidang import daftarSidangs


class Prodis(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama_prodi = db.Column(db.String(230), unique=True, nullable=False)
    fakultas = db.Column(db.String(60), index=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    daftarsidangs = db.relationship("daftarSidangs",
                            lazy='select',
                            backref=db.backref('daftarsidangs', lazy='joined'))

    def __repr__(self):
        return '<Prodi {}>'.format(self.nama_prodi)