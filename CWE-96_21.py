#2.# Example 2: Unrestricted File Upload

from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    # Vulnerable line: file.save(file.filename)
    # Description: This code is vulnerable to unrestricted file upload as it allows any file to be uploaded and saved to the server without proper validation.