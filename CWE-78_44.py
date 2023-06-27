#5.# Example 5: Unrestricted File Upload

from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('/home/user/uploads/' + file.filename)
    return "File uploaded successfully!"

# Vulnerable line: file.save('/home/user/uploads/' + file.filename)
# Description: This code is vulnerable to unrestricted file upload as it allows a user to upload any file to the server without proper validation.