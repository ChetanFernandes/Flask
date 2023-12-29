from flask import Flask
from flask import render_template, request, session, redirect, url_for


app = Flask(__name__)

users = {
    "Chetan":{
        "username": "Chetan",
        "email": "chetan@gmail.com",
        "password" : "1234",
        "bio" : "Learning Python"
    },
    "Sheryl":{
        "username":"Sheryl",
        "email" : "guide@email.com",
        "password":"abcd",
        "bio":"I am good",
        
    },

}


app.config["SECRET_KEY"] = "CHETAN"

@app.route("/sign-in")
def main123():
    return render_template("public/child_session_sign_in.html")

@app.route("/sign-in", methods = ["GET","POST"])
def sign_in():
    if request.method == "POST":
        req = request.form

        username = request.form["username"]
        password = req.get("password")
       

        if not username in users:
            return "User not found"
            return redirect("/sign-in")
        else:
            user = users[username]

      
        if not password == user["password"]:
            return "Password Incorrect"
            return redirect("/sign-in")
        else:
            #Creating a keya and value for session
            session["USERNAME"] = user["username"]
            return redirect("/profile1")

    return render_template("public/child_session_sign_in.html")

@app.route("/profile1")
def profile1():
    if session.get("USERNAME", None) is not None:
        username = session.get("USERNAME")
        user = users[username]
        return render_template("public/child_profile.html", user=user)
    else:
        print("Username not found in session")
        return redirect("/sign-in")

@app.route("/sign-out")
def sign_out():
    session.pop("USERNAME",None)
    return redirect("/sign-in")


if __name__ =="__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)