#8.# Example 8: Broken Access Control

from flask import Flask, request

app = Flask(__name__)

@app.route('/admin')
def admin():
    if request.args.get('admin') == 'true':
        # Vulnerable line: return "Welcome, admin!"
        # Description: This code has broken access control as it allows anyone to access the admin page by simply adding '?admin=true' to the URL.
        return "Welcome, admin!"
    else:
        return "Access denied"