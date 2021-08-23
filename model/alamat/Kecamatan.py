from main import db

class Kecamatan(db.Model):
    __tablename__ = 'kecamatan'

    id = db.Column(db.Integer, primary_key=True)
    kabupaten_id = db.Column(db.Integer, db.ForeignKey('kabupaten.id'))
    nama = db.Column(db.String())
    kabupaten = db.relationship('Kabupaten', backref='kabupaten', lazy=True)

    # def __init__(self):
    #     pass

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def list(self, kab_id):
        return [
            {
                "id": row.id,
                "nama": row.nama,
            } 
        for row in Kecamatan().query.filter_by(kabupaten_id=kab_id).order_by(self.nama)]