#9.# Example 9: Insufficient Session Expiration

from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password':
        session['logged_in'] = True
        return "Logged in successfully"
    else:
        return "Invalid credentials"

@app.route('/admin')
def admin():
    if session.get('logged_in'):
        # Vulnerable line: return "Welcome, admin!"
        # Description: This code is vulnerable to insufficient session expiration as it allows users to access the admin page even after logging out.
        return "Welcome, admin!"
    else:
        return "Access denied"