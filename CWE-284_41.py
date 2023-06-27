#2.# Example 2: Unrestricted File Upload

from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('/uploads/' + file.filename)

    # Vulnerable line: file.save('/uploads/' + file.filename)
    # Description: This code is vulnerable to unrestricted file upload as it allows users to upload any file to the server without proper validation.