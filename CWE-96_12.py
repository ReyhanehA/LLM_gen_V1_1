#3.# CWE-96: Improper Neutralization of Directives in Statically Saved Code (XSS)

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    return "Hello " + name + "!"

# The vulnerable line is line 6 where user input is directly concatenated with a string without proper sanitization, allowing for potential XSS attacks.