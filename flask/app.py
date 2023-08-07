from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "this is fun"

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
