#10.# Insufficient Session Expiration:


from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        session['logged_in'] = True
        return 'Logged in successfully!'
    else:
        return 'Invalid username or password.'

@app.route('/admin')
def admin():
    if session.get('logged_in'):
        return 'Welcome, admin!'
    else:
        return 'Access denied.'

if __name__ == '__main__':
    app.run()

# The vulnerable line is the lack of proper session expiration, allowing for session hijacking attacks.