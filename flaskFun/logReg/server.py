from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
from flask.ext.bcrypt import generate_password_hash
import re
import bcrypt


# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "donotsharesecret"

mysql = MySQLConnector(app, 'logReg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
	form = request.form
	errors = []

	if len(form['first_name']) == 0:
		errors.append('Please enter your first name.')
	elif len(form['first_name']) < 2:
		errors.append('Your first name must be more than 1 letter long.')
	elif not form['first_name'].isalpha():
		errors.append('Your first name may only contain letters.')	

	if len(form['last_name']) == 0: 
		errors.append('Please enter your last name.')
	elif len(form['last_name']) < 2:
		errors.append('Your last name must be more than 1 letter long.')
	elif not form['last_name'].isalpha():
		errors.append('Your last name may only contain letters.')

	if len(form['email']) == 0: 
		errors.append('Please enter your email.')
	elif not EMAIL_REGEX.match(form['email']):
		errors.append("Please enter a valid format email address 'name@domain.us'")

	if len(form['password']) == 0:
		errors.append('Please choose a password')
	elif len(form['password']) < 8:
		errors.append('Please choose a password greater than 7 characters')
	elif form['password'] != form['passconf']:
		errors.append('Please make sure your passwords match')

	if len(errors) > 0: 
		for error in errors:
			flash(error,'errors')
	else:
		check_email = mysql.query_db('SELECT * FROM users WHERE email = :email', {'email': form['email']})
		if len(check_email) > 0:
			flash("Account at that email already exists")

		else:
			query = """INSERT INTO users (first_name, last_name, email, password, 
			created_at, updated_at) VALUES (:first_name, :last_name, :email, 
			:password, NOW(), NOW())"""
			
			pw_hash = bcrypt.generate_password_hash('password')
			
			data = {
				'first_name': form['first_name'],
				'last_name': form['first_name'],
				'email': form['email'],
				'password': pw_hash
			}
		
			try: 
				user_id= mysql.query_db(query, data)
				flash("Congratulations! You are now registered. Please login to continue.")
			except: 
				flash("Something is wrong. Please check errors:","errors")

	return redirect('/') 

@app.route('/login', methods=["POST"])
def login():
	form = request.form
	if EMAIL_REGEX.match(form['email']):
		users = mysql.query_db('SELECT * FROM users WHERE email = :email',{'email': form['email']})
		if len(users) > 0:
			user = users[0]
			if bcrypt.check_password_hash(user['password'], form['password']):
				session['current_user'] = user['id']
				flash("Welcome", "success")
				return redirect('/success')

	flash('Invalid credentials. Please try again', 'errors')
	return redirect('/')

@app.route('/success')
def success():
    if 'current_user' not in session:
        flash("You must be logged in to go there!", "errors")
        return redirect('/')

    current_user = mysql.query_db("SELECT * FROM users WHERE id = :id", {"id": session['current_user']})
    return render_template('success.html', user=current_user[0])

@app.route('/theWall')
def theWall():
	if 'current_user' not in session:
		flash("You must be logged in to go there!", "errors")
        return redirect('/')

	current_user = mysql.query_db("SELECT * FROM users WHERE id = :id", {"id": session['current_user']})
	return render_template('theWall.html', user=current_user[0])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
