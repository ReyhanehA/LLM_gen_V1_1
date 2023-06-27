#10.# Broken access control vulnerability in Python code:


from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    if 'username' in session:
        return "Hello, " + session['username'] + "!"
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['username'] = request.form['username']
            return redirect(url_for('admin'))
        else:
            return "Invalid credentials"
    return '''
        <form method="post">
            <input type="text" name="username">
            <input type="password" name="password">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/admin')
def admin():
    if 'username' in session and session['username'] == 'admin':
        return "Welcome, admin!"
    else:
        return redirect(url_for('login'))

# Vulnerable line: if 'username' in session and session['username'] == 'admin':