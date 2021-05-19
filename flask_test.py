from flask import flask ,request,render_template,redirect
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(_file))

myapp = flask(_name_)

@myapp.route("/")
def homepage():
    return render_template("homepage.html")

@nyapp.route("/", methods = ["post"])
def checklogin():
    UN = request.form['username']
    PN = request.form['password']

    sqlconnection = sqlite3.Connection(currentlocation + "\Login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT username, password from users WHERE username = {un} AND password = {pn})".format(un = UN , pn = PN )

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) ==1:
       return render_template("loggedin.html")
    else:
        return redirect("/register")

@myapp.route("/register", methods = ["GET","POST"])
def registerpage():
    if request.method == "POST":
        dUN = request.form['Dusername']
        dPW = request.form['Dpassword']
        Uemail = request.form['Emailuser']
        sqlconnection = sqlite3.Connection(currentlocation = "\login.db")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO Users VALUES('{u}','{p}','{e}')".format(u = dUN, p = dPW, e = Uemail)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/")
    return render_template("Register.html")


if _name_ == "_main_":
   myapp.run()
