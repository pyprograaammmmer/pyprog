from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/puppy")
def kittens():
    return render_template("puppy.html")

if __name__=="__main__":
    app.run(debug=True)
