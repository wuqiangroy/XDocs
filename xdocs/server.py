import os

from flask import Flask, request, jsonify
from flask import send_from_directory

app = Flask(__name__)
app.config['DEBUG'] = True
app.cwd = os.getcwd()


@app.route('/')
def index():
    return send_from_directory(app.cwd + "/client/", "index.html")


@app.route('/docs/<path:path>')
def docs(path):
    return send_from_directory(app.cwd + '/docs/', path)


@app.route('/api/<resources>/', methods=['GET'])
def list(resources):
    return jsonify({resources: request.method})


@app.route('/api/<resources>/', methods=['POST'])
def create(resources):
    return jsonify({resources: request.method})


@app.route('/api/<resources>/<resource_id>/', methods=['GET'])
def retrieve(resources, resource_id):
    return jsonify({resources: "dassssssasda" + request.method})


@app.route('/api/<resources>/<resource_id>/', methods=['PUT'])
def replace(resources, resource_id):
    return jsonify({resources: resource_id + request.method})


@app.route('/api/<resources>/<resource_id>/', methods=['PATCH'])
def update(resources, resource_id):
    return jsonify({resources: resource_id + request.method})


@app.route('/api/<resources>/<resource_id>/', methods=['DELETE'])
def delete(resources, resource_id):
    return jsonify({resources: resource_id + request.method})
