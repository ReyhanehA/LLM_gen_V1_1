#10.# Example 10: Cross-Site Request Forgery (CSRF)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form['amount']
    account = request.form['account']
    # Transfer money to account

# Vulnerable line: amount = request.form['amount']
# Description: This code is vulnerable to CSRF as it does not include any CSRF protection mechanisms, which could allow an attacker to trick a user into making a transfer without their knowledge or consent.