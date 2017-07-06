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

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	email = request.form['email']
	print name
	print email
	return render_template('process.html',name=name, email=email)

app.run(debug=True)
