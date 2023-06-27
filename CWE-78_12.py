#3.# Example 3: Cross-Site Scripting (XSS)

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', '')
    message = "Hello, " + name + "!"
    template = "<h1>{{ message }}</h1>"
    return render_template_string(template, message=message)

# CWE-78: The user input is not properly sanitized and can be used to inject malicious scripts
# Vulnerable line: message = "Hello, " + name + "!"