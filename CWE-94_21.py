#3.# Example 3: Cross-Site Scripting (XSS)

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', '')
    message = "Hello, " + name + "!"
    return render_template_string("<h1>{{ message }}</h1>")

# Vulnerable line: message = "Hello, " + name + "!"
# Description: This code is vulnerable to XSS as it concatenates user input directly into the HTML template without proper sanitization.