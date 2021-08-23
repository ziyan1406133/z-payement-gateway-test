from app import db

import locale
locale.setlocale( locale.LC_ALL, 'id_ID' )

class Produk(db.Model):
    __tablename__ = 'produk'

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String())
    harga = db.Column(db.Integer())
    # is_active = db.Column(db.SmallInteger())

    # def __init__(self):
    #     pass

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def list(self):
        return [
            {
                "id": row.id,
                "nama": row.nama,
                "harga": locale.currency( row.harga, grouping=True )
            } 
        for row in Produk().query.all()]

    
    def store(self, data):
        try:
            produk = Produk()
            produk.nama = data["nama"]
            produk.harga = data["harga"]

            db.session.add(produk)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            return False
    
    def update(self, data, id):
        try:
            produk = Produk().query.get(id)
            produk.nama = data["nama"]
            produk.harga = data["harga"]
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            return False
    
    def destroy(self, id):
        try:
            produk = Produk().query.get(id)
            db.session.delete(produk)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            return False