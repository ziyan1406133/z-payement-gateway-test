from app import db

class Kelurahan(db.Model):
    __tablename__ = 'kelurahan'

    id = db.Column(db.BigInteger, primary_key=True)
    kecamatan_id = db.Column(db.Integer, db.ForeignKey('kecamatan.id'))
    nama = db.Column(db.String())
    kecamatan = db.relationship('Kecamatan', backref='kecamatan', lazy=True)

    # def __init__(self):
    #     pass

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def list(self, kec_id):
        return [
            {
                "id": row.id,
                "nama": row.nama,
            } 
        for row in Kelurahan().query.filter_by(kecamatan_id=kec_id).order_by(self.nama)]