from flask import Flask, render_template

app = Flask(__name__)

@app.route("/Homepage")
def route():
    return render_template("public/child_static.html")

@app.route("/Flask")
def Falsk():
    return render_template("public/child_Flask.html")


#Navigation for "About" in Homepage
@app.route("/about")
def index():
    return render_template("public/child_index.html")

#Navigation for "Admin" in Homepage
@app.route("/adminpage")
def admin():
    return render_template("admin/child_admin_home_page.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/child_dashboard.html")

@app.route("/admin/profile")
def admin_profile():
    return render_template("admin/child_profile.html")


if __name__ =="__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)