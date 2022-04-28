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
    session['g_answer1'] = request.form['smallercont']
    session['g_answer2'] = request.form['tallestmt']
    session['g_answer3'] = request.form['greatestpop']
    session['g_answer4'] = request.form['capitalstate']
    g_correct = 0
    g_score = ""

    
    return render_template("math.html")

@app.route("/history", methods=['GET', 'POST'])
def render_history():
    session['g_answer1'] = request.form['easy']
    session['g_answer1'] = request.form['quad']
    session['g_answer1'] = request.form['prime']
    session['g_answer1'] = request.form['sqandcb']
    m_correct = 0
    m_score = ""
    
    return render_template("history.html")


@app.route("/results", methods=['GET', 'POST'])
def render_results(): 
    g_correct1 = 'Australia'
    g_correct2 = 'Mt. Everest'
    g_correct3 = 'China'
    g_correct4 = 'Washington D.C.'
    m_correct1 = '2'
    m_correct2 = 'ax^2 + bx + c'
    m_correct3 = '67'
    m_correct4 = '64'
    h_correct1 = '7th Century BC'
    h_correct2 = 'Australia'
    h_correct3 = 'Australia'
    h_correct4 = 'Australia'
    h_answ1 = request.form['wallchina']
    h_answ2 = request.form['xmastruce']
    h_answ3 = request.form['plaguestart']
    h_answ4 = request.form['romanfall']
    fname = request.form['fname']
    lname = request.form['lname'] 
    h_correct = 0
    h_score = ""
    total="/4"
    
    if g_answ1 == g_correct1:
        g_correct = g_correct+1
    if g_answ2 == g_correct2:
        g_correct = g_correct+1
    if g_answ3 == g_correct3:
        g_correct = g_correct+1
    if g_answ4 == g_correct4:
        g_correct = g_correct+1
    g_score = g_correct + total
    if m_answ1 == m_correct1:
        m_correct = m_correct+1
    if m_answ2 == m_correct2:
        m_correct = m_correct+1
    if m_answ3 == m_correct3:
        m_correct = m_correct+1
    if m_answ4 == m_correct4:
        m_correct = m_correct+1
    m_score = m_correct + total
    if h_answ1 == h_correct1:
        h_correct = h_correct+1
    if h_answ2 == h_correct2:
        h_correct = h_correct+1
    if h_answ3 == h_correct3:
        h_correct = h_correct+1
    if h_answ4 == h_correct4:
        h_correct = h_correct+1
    h_score = h_correct + total
    
    if request.method == "POST":
        return render_template("results.html", uFname=fname, uLname=lname, uGeography=g_score, uMath=m_score, uHistory=h_score)
    else:
        session.clear()
        return redirect("/")
    

@app.route("/startover", methods=['GET', 'POST'])
def render_restart():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)