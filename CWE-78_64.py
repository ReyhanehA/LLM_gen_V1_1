#8.# Unrestricted file upload vulnerability in Python code:


from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('/home/user/uploads/' + file.filename)
        return redirect(url_for('index'))
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''

# Vulnerable line: file.save('/home/user/uploads/' + file.filename)