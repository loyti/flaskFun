from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)

mysql = MySQLConnector(app,'friendsdb')
app.secret_key = "keepSecretSafe"
@app.route('/')
def index():
 	query = "SELECT * FROM friends"                           # define your query
	friends = mysql.query_db(query)                           # run query with query_db()
	return render_template('index.html', all_friends=friends) # pass data to our template


@app.route('/friends', methods=['POST'])
def create():
	if (request.form['first_name'] == "") or (request.form['last_name'] == "") or (request.form['age'] == "") or (request.form['friendSince'] == "") or (request.form['occupation'] == ""):
                flash("You must complete all fields!")
        # else if email doesn't match regular expression display an "invalid email address" message
        else:
                flash("Success!")
	# Write query as a string. Notice how we have multiple values
	# we want to insert into our query.
		query = "INSERT INTO friends (first_name, last_name, age, friendSince, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :age, :friendSince, :occupation, NOW(), NOW())"
	# We'll then create a dictionary of data from the POST data received.
		data = {
			'first_name': request.form['first_name'],
			'last_name':  request.form['last_name'],
			'age': request.form['age'],
			'friendSince': request.form['friendSince'],
			'occupation': request.form['occupation']
		}
	
		print request.form['first_name']
		print request.form['last_name']
		print request.form['age']
		print request.form['friendSince']
		print request.form['occupation']

	# add a friend to the database!

		mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<friend_id>')
def show(friend_id):
	# Write query to select specific user by id. At every point where
	# we want to insert data, we write ":" and variable name.
	query = "SELECT * FROM friends WHERE id = :specific_id"
	# Then define a dictionary with key that matches :variable_name in query.
	data = {'specific_id': friend_id}
	# Run query with inserted data.
	friends = mysql.query_db(query, data)
	# Friends should be a list with a single object,
	# so we pass the value at [0] to our template under alias one_friend.
	return render_template('index.html', one_friend=friends[0])

@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, age = :age, friendSince = :friendSince, occupation = :occupation WHERE id = :id"
	data = {
		'first_name': request.form['first_name'],
		'last_name':  request.form['last_name'],
		'age': request.form['age'],
		'friendSince': request.form['friendSince'],
		'occupation': request.form['occupation'],
		'id': friend_id
	}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
	query = "DELETE FROM friends WHERE id = :id"
	data = {'id': friend_id}
	mysql.query_db(query, data)
	return redirect('/')


app.run(debug=True)
