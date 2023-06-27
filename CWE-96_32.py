#5.# Unvalidated Redirects and Forwards:


from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/redirect')
def redirect_to_url():
    url = request.args.get('url')
    return redirect(url)

# The vulnerable line is the redirect call where user input is not properly validated, allowing for unvalidated redirects and forwards.