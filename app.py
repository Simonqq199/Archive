import os  
from flask import Flask, request, Response, render_template, send_from_directory
  
app = Flask(__name__)  
app.config['UPLOAD_FOLDER'] = 'uploads'  
  
@app.route('/')  
def home():  
    return 'Hello, World!'  
  
@app.route('/upload', methods=['POST'])  
def upload_file():  
    file = request.files['file']  
    # Save the file to the uploads folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))  
    return 'File uploaded successfully'  
  
@app.route('/download', methods=['GET', 'POST'])
def download_file():
    if request.method == 'POST':
        filename = request.form['filename']
        directory = app.config['UPLOAD_FOLDER']
        return send_from_directory(directory, filename, as_attachment=True)
    return render_template('download.html')
  
@app.route('/upload-form')  
def upload_form():  
    return render_template('upload.html')
  
if __name__ == '__main__':  
    app.run(debug=True)
