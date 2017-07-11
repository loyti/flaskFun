from flask import Flask, render_template, redirect, request, session, flash
import random

app = Flask(__name__)
app.secret_key = "secretKey"

@app.route('/')
def index():
	session["win"] = session.get("win", 0)
	session["loss"] = session.get("loss", 0)
	session["tie"] = session.get("tie", 0)
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route("/process_play", methods=["POST"])
def process_play():
    opponentHand = random.randint(0,2)
    arrayHand = ["rock", "paper", "scissors"]
    opponent = arrayHand[opponentHand]
    session["opponentOut"] = opponent
    session["playerHand"] = request.form["hand"]
    if session["playerHand"] == opponent:
        session["tie"] += 1
        session["outcome"] = "tie"
    elif session["playerHand"] == "rock":
        if opponent == "paper":
            session["loss"] += 1
            session["outcome"] = "loss"
        elif opponent == "scissors":
            session["win"] += 1
            session["outcome"] = "win"
    elif session["playerHand"] == "paper":
        if opponent == "rock":
            session["win"] += 1
            session["outcome"] = "win"
        elif opponent == "scissors":
            session["loss"] += 1
            session["outcome"] = "loss"
    elif session["playerHand"] == "scissors":
        if opponent == "rock":
            session["loss"] += 1
            session["outcome"] = "loss"
        elif opponent == "paper":
            session["win"] += 1
            session["outcome"] = "win"
    return redirect("/")

@app.route("/endGame", methods=["POST"])
def endGame():
    session.pop("win")
    session.pop("loss")
    session.pop("tie")
    return redirect("/")

@app.route('/process_survey', methods=['POST'])
def process_survey():
	print request.form
	session['name'] = request.form['name']
	session['dojoLoc'] = request.form['dojoLoc']
	session['favLang'] = request.form['favLang']
	session['comment'] = request.form['comment']
	cFormVerify = [session['name'], session['dojoLoc'], session['favLang'], session['comment']]
	
	if len(request.form['name']) < 1:
                flash('Name cannot be empty!')
		return redirect('/survey')
        else:
                flash('Success! Your name is {}'.format(request.form['name']))
        if len(request.form['dojoLoc']) < 1:
                flash('Dojo Location cannot be empty!')  
                return redirect('/survey')
        else:
                flash('Success! Your Dojo Location is {}'.format(request.form['dojoLoc']))
	if len(request.form['favLang']) < 1:
                flash('Favorite Language cannot be empty!')  
                return redirect('/survey')
        else:
                flash('Success! Your Favorite Language is {}'.format(request.form['favLang']))
	if len(request.form['comment']) < 1: 
		flash('There are no comments')
		return redirect('/survey')
	else:
		flash('Your comments: {}'.format(request.form['comment']))
	return redirect('/survey')

@app.route('/survey')
def survey():
	name = session['name']
        dojoLoc = session['dojoLoc']
        favLang = session['favLang']
        comment = session['comment']
	return render_template('/survey.html')

app.run(debug=True)
