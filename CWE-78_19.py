#10.# Example 10: HTML Injection

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', '')
    message = "Hello, " + name + "!"
    template = "<h1>" + message + "</h1>"
    return render_template_string(template)

# CWE-78: The user input is not properly sanitized and can be used to inject HTML tags
# Vulnerable line: template = "<h1>" + message + "</h1>"