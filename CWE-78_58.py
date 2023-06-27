#2.# Cross-site scripting (XSS) vulnerability in Python code:


from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', '')
    message = "Hello, " + name + "!"
    return render_template_string("<h1>{{ message }}</h1>")

# Vulnerable line: return render_template_string("<h1>{{ message }}</h1>")