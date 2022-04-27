from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
import os

app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]

@app.route("/")
def render_home():
    return render_template("home.html")

@app.route("/geography", methods=['GET', 'POST'])
def render_geography():
    if request.method == "POST":
        return render_template("geography.html")
    else:
        session.clear()
        return redirect("/")

@app.route("/math", methods=['GET', 'POST'])
def render_math():
    return render_template("math.html")

@app.route("/history", methods=['GET', 'POST'])
def render_history():
    return render_template("history.html")

@app.route("/results", methods=['GET', 'POST'])
def render_results():
    return render_template("results.html")

@app.route("/startover", methods=['GET', 'POST'])
def render_restart():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=False)