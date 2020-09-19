from app import db
from datetime import datetime
from app.model.sidang import Sidangs


class SidangFiles(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    file_name = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    sidang_id = db.Column(db.BigInteger, db.ForeignKey(Sidangs.id))
    sidangs = db.relationship("Sidangs", backref="sidang_id")



    def __repr__(self):
        return '<Sidang {}>'.format(self.nama_mhs)