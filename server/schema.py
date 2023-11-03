from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer (db.Model):
    cust_id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Item (db.Model):
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_title = db.Column(db.String(32), nullable=False)
    item_desc = db.Column(db.String(128), nullable=True)

    price = db.Column(db.Double, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__ (self, title, price, quant):
        self.item_title = title
        self.price = price
        self.quantity = quant

orders = db.Table('orders',
    db.Column('order', db.Integer, db.ForeignKey('invoice.invoice_id')),
    db.Column('amount', db.Integer),
    db.Column('item', db.Integer, db.ForeignKey('item.item_id'))              
)

class Invoice (db.Model):
    invoice_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    total_before_tax = db.Column(db.Double, nullable=False, autoincrement=True)

    items = db.relationship('Item', secondary='orders')
