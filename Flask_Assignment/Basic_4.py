from flask import Flask
from flask import render_template
from flask import  request, redirect, make_response, jsonify
import requests

app = Flask(__name__)

@app.route("/sign-up", methods =["GET","POST"])
def sign_up():
    if request.method == "POST":
        req = request.form
        #types of getting data
        username = req["username"]
        email = req.get("email")
        password = request.form["password"]
        city = request.form.get("city")
        res = make_response(jsonify(req),200)
        return res

    return render_template("public/child_sign_up.html")

if __name__ =="__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)
