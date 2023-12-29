# Basics of Flask
# Create a Flask app that displays "Hello World" on home page
from flask import Flask, request
import logging
logging.basicConfig(filename = "error.log", level = logging.DEBUG, format = '%(asctime)s = %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route("/")
def display():
    return f"Hello World"

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0", port = "5002")
