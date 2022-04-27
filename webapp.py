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
    g_correct = 'Australia'
    g_correct = 'Mt. Everest'
    g_correct = 'China'
    g_correct = 'Washington D.C.'
    m_correct = '2'
    m_correct = 'ax^2 + bx + c'
    m_correct = '67'
    m_correct = '64'
    h_correct = '7th Century BC'
    h_correct = 'Australia'
    h_correct = 'Australia'
    h_correct = 'Australia'
    g_answ1 = request.forms['smallercont']
    g_answ2 = request.forms['tallestmt']
    g_answ3 = request.forms['greatestpop']
    g_answ4 = request.forms['capitalstate']
    m_answ1 = request.forms['easy']
    m_answ2 = request.forms['quad']
    m_answ3 = request.forms['prime']
    m_answ4 = request.forms['sqandcb']
    h_answ1 = request.forms['wallchina']
    h_answ2 = request.forms['xmastruce']
    h_answ3 = request.forms['plaguestart']
    h_answ4 = request.forms['romanfall']
    
    
    return render_template("results.html")

@app.route("/startover", methods=['GET', 'POST'])
def render_restart():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=False)