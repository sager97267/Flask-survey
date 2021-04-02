from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey 


app=Flask(__name__)
app.config['SECRET_KEY']="jhfldasufadfhaoui"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug=DebugToolbarExtension(app)

responses=[]
@app.route('/')
# creating home page route for survey
def home_page():
    
    return render_template('index.html',survey=survey)

@app.route('/start')
def start():
    return redirect('/question/0')
   
    # return render_template('question.html',survey=survey)

@app.route('/question/<int:num>')
def question(num):
    # num=request.args.get('num')
    return render_template('question.html',survey=survey,num=num)

@app.route('/question2')
def question2():
    # awnser2=request.form['awnser']
    # responses.append(awnser2)
    return render_template('question2.html',survey=survey)

@app.route('/question3')
def question3():
    # awnser3=request.form['awnser']
    # responses.append(awnser3)
    return render_template('question3.html',survey=survey)

@app.route('/question4')
def question4():
    # awnser4=request.form['awnser']
    # responses.append(awnser4)
    return render_template('question4.html',survey=survey)

@app.route('/compleat')
def survay_compleated():
    return render_template('compleat.html',responses=responses)
# @app.route('/question2')
# def question2():
#     return render_template('/question3.html',survey=survey)
    

@app.route('/awnser', methods=["POST"])
def collect_awnsers():
    awnser=request.form['awnser']
    responses.append(awnser)

    if len(responses)==4:
        return redirect('/compleat')

    else:
        return redirect(f'question/{len(responses)}')




