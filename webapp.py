from django.shortcuts import render
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
import os

app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]

@app.route("/", methods=['GET', 'POST'])
def render_home():
    if 'userFname' not in session:
        return render_template("home.html")
    else:
        return redirect(url_for('render_geography'), code=307)

@app.route("/geography", methods=['GET', 'POST'])
def render_geography():
    if request.method == "POST":
        if 'userFname' not in session:  
            # User's First and Last Name 
            session['userFname'] = request.form['fname']
            session['userLname'] = request.form['lname']   
            return render_template("geography.html")
        else:
            return redirect(url_for('render_math'), code=307)

    else:
        session.clear()
        return redirect("/")

@app.route("/math", methods=['GET', 'POST'])
def render_math():
    if request.method == "POST":
        if 'g_answer1' not in session:
            # User Answers Geography
            session['g_answer1'] = request.form['smallercont']
            session['g_answer2'] = request.form['tallestmt']
            session['g_answer3'] = request.form['greatestpop']
            session['g_answer4'] = request.form['capitalstate']
            return render_template("math.html")
        
        elif 'm_answer1' in session:
            return redirect(url_for('render_history'), code=307)
        
        elif 'g_answer' in session:
            return render_template("math/html")
            
        
        
    else:
        session.clear()
        return redirect("/")

@app.route("/history", methods=['GET', 'POST'])
def render_history():
    if request.method == "POST":      
        if 'm_answer1' not in session:
            # User Answers Math
            session['m_answer1'] = request.form['easy']
            session['m_answer2'] = request.form['quad']
            session['m_answer3'] = request.form['prime']
            session['m_answer4'] = request.form['sqandcb']
            return render_template("history.html")
        
        elif 'h_answer1' in session:
            return redirect(url_for('render_results'), code=307) 
        
        else:
            return render_template("history.html")
            
        
    else:
        session.clear()
        return redirect("/")
    


@app.route("/results", methods=['GET', 'POST'])
def render_results():    
    if request.method == "POST":
        if 'h_answer1' not in session:
            # User Answers History
            session['h_answer1'] = request.form['wallchina']
            session['h_answer2'] = request.form['xmastruce']
            session['h_answer3'] = request.form['plaguestart']
            session['h_answer4'] = request.form['romanfall']
        
            # Answer Key
            g_correct1 = 'Australia'
            g_correct2 = 'Mt. Everest'
            g_correct3 = 'China'
            g_correct4 = 'Washington D.C.'
            m_correct1 = '2'
            m_correct2 = 'ax^2 + bx + c'
            m_correct3 = '67'
            m_correct4 = '64'
            h_correct1 = '7th Century BC'
            h_correct2 = 'World War 1'
            h_correct3 = '1364'
            h_correct4 = '395 AD'
            
            # Used for Displaying Score
            g_correct = 0
            g_score = ""
            m_correct = 0
            m_score = ""
            h_correct = 0
            h_score = ""
            
            total="/4"
            # Determine Geography Score
            if g_correct1 in session["g_answer1"]:
                g_correct = g_correct + 1
            if g_correct2 in session["g_answer2"]:
                g_correct = g_correct + 1
            if g_correct3 in session["g_answer3"]:
                g_correct = g_correct + 1
            if g_correct4 in session["g_answer4"]:
                g_correct = g_correct + 1
            g_score = str(g_correct) + total
            
            # Determine Math Score
            if m_correct1 in session["m_answer1"]:
                m_correct = m_correct + 1
            if m_correct2 in session["m_answer2"]:
                m_correct = m_correct + 1
            if m_correct3 in session["m_answer3"]:
                m_correct = m_correct + 1
            if m_correct4 in session["m_answer4"]:
                m_correct = m_correct + 1
            m_score = str(m_correct) + total
            
            # Determine History Score
            if h_correct1 in session["h_answer1"]:
                h_correct = h_correct + 1
            if h_correct2 in session["h_answer2"]:
                h_correct = h_correct + 1
            if h_correct3 in session["h_answer3"]:
                h_correct = h_correct + 1
            if h_correct4 in session["h_answer4"]:
                h_correct = h_correct + 1
            h_score = str(h_correct) + total
        
            return render_template("results.html", uFname=session['userFname'], uLname=session['userLname'], uGeography=g_score, uMath=m_score, uHistory=h_score)
    
    else:
        session.clear()
        return redirect("/")
    

@app.route("/startover", methods=['GET', 'POST'])
def render_restart():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)