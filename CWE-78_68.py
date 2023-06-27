#2.# Cross-Site Scripting (XSS):


from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    template = "<h1>Hello, {{ name }}!</h1>"
    return render_template_string(template, name=name)

if __name__ == '__main__':
    app.run()


# The vulnerable line is line 8, where user input is directly rendered as HTML without proper escaping, allowing for XSS attacks.