from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector

import re
# create a regular expression object that we can use run operations on

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)

mysql = MySQLConnector(app,'eValid')
app.secret_key = "donotsharesecret"

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/success', methods=['POST'])
def submit():
	if len(request.form['email']) < 1:
		flash("Email must be in correct format 'name@domain.us'")
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Email must be in correct format 'name@domain.us'")
		return redirect('/')
	else:
		flash("Congratulations! You've successfully registered!")
		query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
		data = {
                        'email': request.form['email'],
                }
		mysql.query_db(query, data)
		return redirect('/success')

@app.route('/success', methods=['GET'])
def success():
	query = "SELECT * FROM emails"
        emails = mysql.query_db(query)
	return render_template("success.html", all_emails=emails)

app.run(debug=True)
