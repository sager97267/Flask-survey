from flask import Flask,request,render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey 


app=Flask(__name__)
app.config['SECRET_KEY']="jhfldasufadfhaoui"

debug=DebugToolbarExtension(app)

@app.route('/home')
def home_page():
    
    return render_template('index.html')







responses=[]