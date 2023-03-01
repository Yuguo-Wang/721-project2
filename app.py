from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        file.save(os.path.join('uploads', filename))
        return jsonify({'success': True, 'message': 'File uploaded successfully'})
    else:
        return jsonify({'success': False, 'message': 'No file uploaded'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
