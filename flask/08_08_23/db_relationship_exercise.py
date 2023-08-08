from flask import Flask, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(50), nullable = False)
    Address = db.Column(db.String(60), nullable = False)
    Delivery = db.Relationship('Delivery', backref='orders')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(60), unique = True)
    Description = db.Column(db.String(100), nullable = False)
    Delivery = db.Relationship('Delivery', backref='products')
    

class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    orders_id = db.Column('orders_id', db.Integer, db.ForeignKey('orders.id'))
    products_id = db.Column('products_id', db.Integer, db.ForeignKey('products.id'))



    @app.route('/')
    def home():
        return "Home"