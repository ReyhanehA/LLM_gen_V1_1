#4.# Example 4: Cross-Site Scripting (XSS)

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', '')
    message = "Hello, " + name + "!"
    return render_template_string("<h1>{{ message }}</h1>")

# Vulnerable line: message = "Hello, " + name + "!"
# Description: This code is vulnerable to XSS as it concatenates user input directly into an HTML template without proper sanitization.