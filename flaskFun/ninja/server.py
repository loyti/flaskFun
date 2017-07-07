from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

app.secret_key = 'RedSoxGOAT'

@app.route('/')
def index():
	return render_template('turtle.html')
def counter():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1

@app.route('/addSession', methods=['POST'])
def increment():
    session['counter'] += 1
    return redirect('/turtle')

@app.route('/reset_count', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/turtle')

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # here we add two properties to session to store the name and email
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return redirect('/show') # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!

@app.route('/show')
def show_user():
  return render_template('user.html', name=session['name'], email=session['email'])


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

@app.route('/turtle/blue')
def blue():
	return render_template('blue.html')

@app.route('/turtle/red')
def red():
	return render_template('red.html')

@app.route('/turtle/orange')
def orange():
	return render_template('orange.html')

@app.route('/turtle/purple')
def purple():
	return render_template('purple.html')

@app.route('/april')
def april():
	return render_template('april.html')

#@app.errorhandler(404)
#def page_not_found(error):
#    return 'This page does not exist', 404
#app.error_handler_spec[None][404] = page_not_found

#@app.errorhandler(404)
#def april():
#        return render_template('april.html')
	
app.run(debug=True)

