from flask import Flask, request, url_for, session, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta


app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes= 2)
app.config["SECRET_KEY"] = "jasabdsadhbj"

# Home page
@app.route("/")
def home():
    # returning the html to display home page 
    return render_template("index.html")

# "login page" resposible to display the login form and take information from the user
@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        
        # received posted information from the form
        user = request.form["user"]
        email = request.form["mail"]

        # created session to pass information through pages
        session["user"] = user
        session["mail"] = email
        
        # The variable makes the session permanent for the time stated
        session.permanent = True

        print(session)

        # message indicating success for on login in
        flash("You logged in successfully")

        
        # redirected the page for the user page in order to reveal data
        return redirect(url_for("user"))

    else:

        # in case of the session alreay hold an user in the server the user will be recirected to user page
        if "user" in session and "mail" in session:
            
            flash("You're already logged in!")
            return redirect(url_for("user"))


        # there's really nothing to get from the files besides the page itself from now
        return render_template("login.html")
    

@app.route("/logout")
def logout():

    # checking if the respective data is stored in the session
    if "user" in session and "mail" in session:
        del session["mail"]
        del session["user"]

        flash("Logged out successfully!")
        return redirect(url_for("home"))
        
@app.route("/user")
def user():

    # checking if the respective data is stored in the session
    if "user" in session and "mail" in session:
        
        usr = session["user"]
        mail = session["mail"]

        # variables that hold the value for data in the session
        return render_template("user.html", name= usr, mail= mail)
    else:
        # if there's no user in the server the user will be redirected to the login page
        flash("There's no user in the server")
        return redirect(url_for("login"))
        



if __name__ == "__main__":
    app.run(debug=True)