#10.# Example 10: Cross-Site Request Forgery (CSRF)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form['amount']
    recipient = request.form['recipient']

    # Vulnerable line: return render_template('transfer.html', amount=amount, recipient=recipient)
    # Description: This code is vulnerable to CSRF as it allows an attacker to craft a malicious form that submits a transfer request on behalf of the user without their knowledge or consent.