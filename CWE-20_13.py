#8.# Example 8: Unrestricted File Upload

from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('/home/user/uploads/' + file.filename)
    return "File uploaded successfully."

if __name__ == '__main__':
    app.run()

# The vulnerable line is line 5 where user input is directly used in a file path without proper validation.
# CWE-20: Improper Input Validation