from flask import Flask, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), default="Mise")
    last_name = db.Column(db.String(30), unique=True)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)




@app.route('/postoption', methods=["GET", "POST"])
def posto():
    response = request.method
    return f"method is {response}"

@app.route('/name/<word>')
def name(word):
    var1 = (word + "<br>") * 5
    return var1



# Flask routes exercise
# ------------------------
@app.route('/square/<int:num>')
def square(num):
    var1 = f"{num * num}"
    return var1

# -------------------------

@app.route('/gotogoogle')
def gotogoogle():
    return redirect ("http://www.google.com")


@app.route('/gotohome')
def gotohome():
    return redirect (url_for("home"))



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
