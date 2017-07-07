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

@app.route('/turtle')
def turtle():
	return render_template('turtle.html')

@app.route('/blue')
def blue():
	return render_template('blue.html')

@app.route('/red')
def red():
	return render_template('red.html')

@app.route('/orange')
def orange():
	return render_template('orange.html')

@app.route('/purple')
def purple():
	return render_template('purple.html')

@app.route('/*')
def april():
	return render_template('april.html')

app.run(debug=True)
