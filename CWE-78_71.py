#5.# Unrestricted File Upload:


from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('/var/www/uploads/' + file.filename)
    return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run()


# The vulnerable line is line 6, where user input is directly concatenated into the file path without proper validation, allowing for unrestricted file upload attacks.