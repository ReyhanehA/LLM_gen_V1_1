#10.# Insufficient Authentication:


from flask import Flask, request, session, redirect

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        session['logged_in'] = True
        return redirect('/admin')
    else:
        return redirect('/login')

@app.route('/admin')
def admin():
    if session.get('logged_in'):
        return "Welcome, admin!"
    else:
        return redirect('/login')

# The vulnerable line is the insufficient authentication where any user can log in as the admin with the username 'admin' and password 'password'.