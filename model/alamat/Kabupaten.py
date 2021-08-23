from app import db

class Kabupaten(db.Model):
    __tablename__ = 'kabupaten'

    id = db.Column(db.Integer, primary_key=True)
    provinsi_id = db.Column(db.Integer, db.ForeignKey('provinsi.id'))
    nama = db.Column(db.String())
    provinsi = db.relationship('Provinsi', backref='provinsi', lazy=True)

    # def __init__(self):
    #     pass

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def list(self, prov_id):
        return [
            {
                "id": row.id,
                "nama": row.nama,
            } 
        for row in Kabupaten().query.filter_by(provinsi_id=prov_id).order_by(self.nama)]