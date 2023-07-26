from flask import Flask
import random

app = Flask(__name__)
First_name = "jay", "andrei", "ramon", "emanuel", "rebeca", "george", "alex", "david"
Last_name = "popescu", "gosling", "evans", "pratt", "hemsworth", "dirver", "roger", "bleacher", "ratatouille"
First = random.choice(First_name)
Last = random.choice(Last_name)

@app.route("/")

def name_gen():
   
    
    return(First + " " + Last)

if __name__ == "__main__":
        app.run(debug = True)