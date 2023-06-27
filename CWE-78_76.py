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

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return 'Logged out successfully!'

if __name__ == '__main__':
    app.run()


# The vulnerable line is line 8, where the session is not properly expired, allowing for session hijacking attacks.