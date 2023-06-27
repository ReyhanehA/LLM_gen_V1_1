#9.# Example 9: JavaScript Injection

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', '')
    message = "Hello, " + name + "!"
    template = "<script>alert('{{ message }}');</script>"
    return render_template_string(template, message=message)

# CWE-78: The user input is not properly sanitized and can be used to inject JavaScript
# Vulnerable line: template = "<script>alert('{{ message }}');</script>"