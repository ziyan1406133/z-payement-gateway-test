from main import db

class User(db.Model):
    __tablename__ = 'user_tbl'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    phone_no = db.Column(db.String())
    provinsi_id = db.Column(db.Integer)
    kabupaten_id = db.Column(db.Integer)
    kecamatan_id = db.Column(db.Integer)
    kelurahan_id = db.Column(db.BigInteger)
    address = db.Column(db.String())

    # def __init__(self):
    #     pass

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def list(self):
        return [
            {
                "id": row.id,
                "first_name": row.first_name,
                "last_name": row.last_name,
                "email": row.email,
                "phone_no": row.phone_no,
                "provinsi_id": row.provinsi_id,
                "kabupaten_id": row.kabupaten_id,
                "kecamatan_id": row.kecamatan_id,
                "kelurahan_id": row.kelurahan_id,
                "address": row.address,
            } 
        for row in User().query.all()]


    def store(self, data):
        try:
            user = User()
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            user.phone_no = data["phone_no"]
            user.provinsi_id = data["provinsi_id"]
            user.kabupaten_id = data["kabupaten_id"]
            user.kecamatan_id = data["kecamatan_id"]
            user.kelurahan_id = data["kelurahan_id"]
            user.address = data["address"]

            db.session.add(user)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            return False
    
    def update(self, data, id):
        try:
            user = User().query.get(id)
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            user.phone_no = data["phone_no"]
            user.provinsi_id = data["provinsi_id"]
            user.kabupaten_id = data["kabupaten_id"]
            user.kecamatan_id = data["kecamatan_id"]
            user.kelurahan_id = data["kelurahan_id"]
            user.address = data["address"]
            
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            return False
    
    def destroy(self, id):
        try:
            user = User().query.get(id)
            db.session.delete(user)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            return False