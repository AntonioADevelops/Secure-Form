from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template("home.html")

@app.route("/geography")
def render_geography():
    return render_template("geography.html")

@app.route("/math")
def render_math():
    return render_template("math.html")

@app.route("/math")
def render_history():
    return render_template("history.html")

@app.route("/complete")
def render_results():
    return render_template("results.html")

@app.route("/startover")
def render_restart():
    # session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=False)