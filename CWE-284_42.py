#3.# Example 3: Cross-Site Scripting (XSS)

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q')
    results = []

    # Vulnerable line: return render_template_string('<h1>Search Results for {{ query }}</h1><ul>{% for result in results %}<li>{{ result }}</li>{% endfor %}</ul>')
    # Description: This code is vulnerable to XSS as it renders user input directly into an HTML template without proper sanitization.
    return render_template_string('<h1>Search Results for {{ query }}</h1><ul>{% for result in results %}<li>{{ result }}</li>{% endfor %}</ul>', query=query, results=results)