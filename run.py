from flask import Flask, request
import os
import uuid
import subprocess


ABS_PATH = os.path.abspath(os.path.dirname(__file__))

def readFromTheFile(id):
    try:
        f = open(os.path.join("buff", id + ".txt"), 'rt')
    except:
        return '{"status":"not found"}'
    status = f.readline().strip()
    if status == "running":
        f.close()
        return '{"status":"running"}'
    elif status == "done":
        url = f.readline().strip()
        result = f.readline().strip()
        f.close()
        return '{"md5":"'+result+'","status":"done","url":"'+url+'"}'
    elif status == "fail":
        f.close()
        return '{"status":"fail"}'
    return status

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def new_task():
    url = request.form['url']
    id = str(uuid.uuid4())
    try:
        email = request.form['email']
        subprocess.Popen(["python3", "src.py", str(id), str(url), str(email)])
    except:
        subprocess.Popen(["python3", "src.py", str(id), str(url)])
    return '{"id":"'+id+'"}\n'

@app.route('/check', methods=['GET'])
def check_task():
    id = request.args.get('id')
    result = readFromTheFile(id)
    return str(result) + "\n"

@app.errorhandler(400)
def bad_request(e):
    return '{"error":"400"}' + "\n"

@app.errorhandler(403)
def fobidden(e):
    return '{"error":"403"}' + "\n"

@app.errorhandler(404)
def not_found(e):
    return '{"error":"404"}' + "\n"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)