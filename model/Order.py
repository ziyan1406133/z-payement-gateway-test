from app import db

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)    
    order_id = db.Column(db.String(255))
    buyer_id = db.Column(db.Integer())
    approval_code = db.Column(db.String(255), nullable=True)
    transaction_time = db.Column(db.DateTime())
    gross_amount = db.Column(db.Float())
    currency = db.Column(db.String(255))
    payment_type = db.Column(db.String(255))
    signature_key = db.Column(db.String(255))
    status_code = db.Column(db.String(255))
    transaction_id = db.Column(db.String(255))
    transaction_status = db.Column(db.String(255))
    fraud_status = db.Column(db.String(255))
    settlement_time = db.Column(db.DateTime(), nullable=True)

    def __init__(self, order_id=None):
        self.order_id = order_id

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def list(self, user_id):
        return [
            {
                "id": row.id,
                "order_id": row.order_id,
                "buyer_id": row.buyer_id,
                "approval_code": row.approval_code,
                "transaction_time": row.transaction_time,
                "gross_amount": row.gross_amount,
                "currency": row.currency,
                "payment_type": row.payment_type,
                "signature_key": row.signature_key,
                "status_code": row.status_code,
                "transaction_id": row.transaction_id,
                "transaction_status": row.transaction_status,
                "fraud_status": row.fraud_status,
                "settlement_time": row.settlement_time,
            } 
        for row in Order().query.filter_by(buyer_id=user_id).all()]


    def update(self, data, new=False):
        try:
            print(data)
            order = Order().query.filter_by(order_id=data["order_id"]).first()
            if order == None:
                new = True
                order = Order()
            order.order_id = data["order_id"]
            order.buyer_id = data["buyer_id"]
            order.approval_code = data["approval_code"] if "approval_code" in data else None
            order.transaction_time = data["transaction_time"]
            order.gross_amount = float(data["gross_amount"])
            order.currency = data["currency"]
            order.payment_type = data["payment_type"]
            order.signature_key = data["signature_key"]
            order.status_code = data["status_code"]
            order.transaction_id = data["transaction_id"]
            order.transaction_status = data["transaction_status"]
            order.settlement_time = data["settlement_time"] if "settlement_time" in data else None
            print(order)

            if new:
                db.session.add(order)

            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            db.session.flush()
            return False
