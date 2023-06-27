#9.# Example 9: Cross-Site Request Forgery (CSRF)

from flask import Flask, request

app = Flask(__name__)

@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form['amount']
    account = request.form['account']
    # Transfer money to the specified account
    return "Money transferred successfully."

# Vulnerable line: amount = request.form['amount']
# Description: This code is vulnerable to CSRF as it does not include any CSRF protection mechanism to prevent unauthorized requests from being made.