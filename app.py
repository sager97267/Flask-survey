from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey 


app=Flask(__name__)
app.config['SECRET_KEY']="jhfldasufadfhaoui"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug=DebugToolbarExtension(app)

@app.route('/home')
# creating home page route for survey
def home_page():
    
    return render_template('index.html',survey=survey)

@app.route('/start')
def question():
    return render_template('question.html')








responses=[]