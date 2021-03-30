from flask import Flask,request
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)
app.config['SECRET_KEY']="jhfldasufadfhaoui"

debug=DebugToolbarExtension(app)

@app.route('/home')
def home_page():
    return "hello!"