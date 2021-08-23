from manage import db

class Provinsi(db.Model):
    __tablename__ = 'provinsi'

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String())

    # def __init__(self):
    #     pass

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def list(self):
        return [
            {
                "id": row.id,
                "nama": row.nama,
            } 
        for row in Provinsi().query.all()]