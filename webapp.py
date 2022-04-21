import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template("home.html")

@app.route("/userinfo")
def render_userquiz():
    return render_template("userinfo.html")

@app.route("/startover")
def render_restart():
    # session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=False)