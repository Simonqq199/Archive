from flask import Flask, request, Response, render_template, send_file, send_from_directory, after_this_request
import os

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

@app.route('/download')
def download_file():
    filename = 'example.pdf'
    file_path = app.config['UPLOAD_FOLDER'] + "/" + filename
    @after_this_request
    def remove_file(response):
        try:
            os.remove(file_path)
        except Exception as error:
            app.logger.error("Error removing downloaded file", error)
        return response
    response = send_file(file_path, as_attachment=True)
    response.headers["Content-Disposition"] = "attachment; filename=" + filename
    return response

@app.route('/upload-form')
def upload_form():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
