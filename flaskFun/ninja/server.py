from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
	return render_template('ninja.html')

@app.route('/dojo')
def dojo():
	return render_template('dojo.html')

app.run(debug=True)
