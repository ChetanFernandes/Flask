from flask import Flask, render_template,request
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add")
def add():
    return render_template("add_student.html")

@app.route("/addrec", methods = ["POST", "GET"])
def save_details():
    if request.method == "POST":
        try:
            req = request.form
            name = request.form["name"]
            email = req.get("email")
            address = request.form.get("address")
            pin = req["pin"]

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO STUDENTS (name,email,address,pin) VALUES (?,?,?,?)",(name,email,address,pin))
                con.commit
                msg = "Record Successfully added"
        except:
                con.rollback()  
                msg = "Error in insert option"  
        finally:  
                return render_template("success.html",msg = msg)  
                con.close()  

@app.route("/view")  
def view():  
    con = sql.connect("database.db")  
    con.row_factory = sql.Row  
    cur = con.cursor()  
    cur.execute("select * from STUDENTS")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)

@app.route("/delete")  
def delete():  
    return render_template("delete.html")  

@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"] 
    print(id) 
    with sql.connect("database.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from STUDENTS where id = ?", id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete.html",msg = msg)  

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0", port = 5000)
