from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/river')
def river():
	return render_template('river.html')

@app.route('/cabin')
def cabin():
	return render_template('cabin.html')

@app.route('/drown')
def drown():
	return render_template('drown.html')

@app.route('/bear')
def bear():
	return render_template('bear.html')

@app.route('/lady')
def lady():
	return render_template('lady.html')

@app.route('/juice')
def juice():
	return render_template('juice.html')

app.run(debug=True)
