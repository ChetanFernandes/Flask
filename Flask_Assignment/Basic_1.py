from flask import Flask

app = Flask(__name__)


@app.route("/")
def route():
    return "<h1 style = 'color: orange'>Hello World</h1>"

if __name__ =="__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)
