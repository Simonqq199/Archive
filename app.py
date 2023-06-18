import os  
from flask import Flask, request, Response, render_template  
  
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
        # Set the file path and name
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  
        # Check if the file exists
        if not os.path.exists(path):  
            return "File not found"  
        # Open the file and send it as a response
        with open(path, 'rb') as f:  
            file = f.read()  
        # Set the Content-Disposition header with the filename of the uploaded file
        headers = {'Content-Disposition': f'attachment; filename={filename}'}
        return Response(file, mimetype='application/octet-stream', headers=headers)  
    return render_template('download.html')
  
@app.route('/upload-form')  
def upload_form():  
    return '''  
        <!doctype html>  
        <html>  
           <body>  
              <h1>Upload file</h1>  
              <form method="POST" action="/upload" enctype="multipart/form-data">  
                 <input type="file" name="file">  
                 <input type="submit" value="Upload">  
              </form>  
           </body>  
        </html>  
    '''  
  
if __name__ == '__main__':  
    app.run(debug=True)
