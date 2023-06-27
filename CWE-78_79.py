#3.# Cross-Site Scripting (XSS):


from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    return render_template_string('<h1>Hello {{ name }}!</h1>')

if __name__ == '__main__':
    app.run()

# The vulnerable line is the render_template_string call where user input is directly rendered as HTML, allowing for XSS attacks.