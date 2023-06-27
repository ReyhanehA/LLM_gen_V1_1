#7.# Example 7: Improper Access Control

from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/admin')
def admin():
    if not request.args.get('admin'):
        abort(401)
    return "Welcome, admin!"

# Vulnerable line: if not request.args.get('admin'):
# Description: This code is vulnerable to improper access control as it relies on a query parameter to determine if a user is an admin, which can be easily manipulated.