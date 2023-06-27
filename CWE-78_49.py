#10.# Example 10: Cross-Site Request Forgery (CSRF)

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("<form method='POST' action='/transfer'><input type='hidden' name='amount' value='100'><button type='submit'>Transfer $100</button></form>")

@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form['amount']
    # Transfer money
    return "Money transferred successfully!"

# Vulnerable line: N/A (vulnerability is in the design of the application)
# Description: This code is vulnerable to CSRF as it allows an attacker to trick a user into making a malicious request without their knowledge or consent.