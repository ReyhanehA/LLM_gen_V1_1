#9.# Insufficient session expiration vulnerability in Python code:


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
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <input type="text" name="username">
            <input type="submit" value="Login">
        </form>
    '''

# Vulnerable line: app.secret_key = 'secret'