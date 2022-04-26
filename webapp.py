from distutils.log import error
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
from flask import flash

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template("home.html")

@app.route("/geography", methods=['GET', 'POST'])
def render_geography():
    if request.method == 'POST':
        return render_template("geography.html")
    else:
        flash("Refreshing the page leads to an incomplete result, please press the restard button to restart the quiz")
        return redirect("/")

@app.route("/math", methods=['GET', 'POST'])
def render_math():
    if request.method == 'POST':
        return render_template("math.html")
    else:
        flash("Refreshing the page leads to an incomplete result, please press the restard button to restart the quiz")
        return redirect("/")
    
@app.route("/history", methods=['GET', 'POST'])
def render_history():
    if request.method == 'POST':
        return render_template("history.html")
    else:
        flash("Refreshing the page leads to an incomplete result, please press the restard button to restart the quiz")
        return redirect("/")

@app.route("/results", methods=['GET', 'POST'])
def render_results():
    if request.method == 'POST':
        return render_template("results.html")
    else:
        flash("Refreshing the page leads to an incomplete result, please press the restard button to restart the quiz")
        return redirect("/")

@app.route("/startover", methods=['GET', 'POST'])
def render_restart():
    # session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=False)