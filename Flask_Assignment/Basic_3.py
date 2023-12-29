from flask import Flask
from flask import render_template
from flask import  request, redirect
import requests

app = Flask(__name__)

users = {
    "mitsuhiko":{
        "name": "Armin Ronacher",
        "bio": "Creator  of Falsk",
        "twitter_handle":"@mitsuhiko"
    },
    "gvanrossum":{
        "name":"Guido Van Rossum",
        "bio":"creator of python progrmming language",
        "twitter_handle":"@gvanrossum"
    },
    "elonmusk":{
        "name":"Elon Musk",
        "bio":"technology entrepreneur invetsor and engineer",
        "twitter_handle":"@elonmusk"
    }
}
#Single Variable
@app.route("/profile/<username>")
def profile(username):
    user = None 
    if username in users:
        user = users[username]
    return render_template("public/child_profile.html",user = user)

#Multiple Variable
@app.route("/multiple/<foo>/<bar>/<baz>")
def multi(foo, bar, baz):
    return f"foo is {foo},bar is {bar}, baz is {baz}"

if __name__ =="__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)


