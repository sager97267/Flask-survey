from flask import Flask,request

app=Flask(__name__)

@app.route('/home')
def home_page():
    return "hello!"