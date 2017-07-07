from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/survey', methods=['POST'])
def survey():
	name = request.form['name']
	dojoLoc = request.form['dojoLoc']
	favLang = request.form['favLang']
	comment = request.form['comment']
	return render_template('survey.html',name=name,dojoLoc=dojoLoc,favLang=favLang,comment=comment)

app.run(debug=True)
