#4.# Example 4: Cross-Site Scripting (XSS)

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    return "<h1>Hello, {}!</h1>".format(name)

if __name__ == '__main__':
    app.run()

# The vulnerable line is line 7 where user input is directly used in an HTML response without proper sanitization.
# CWE-20: Improper Input Validation