import json
import os
import re

from kubernetes import client, config, watch

from flask import Flask, request, jsonify

app = Flask(__name__)
config.load_incluster_config()

@app.route('/', methods=['GET'])
def accept():
    name = os.getenv("POD_NAME")
    namespace = os.getenv("POD_NAMESPACE")
    v1 = client.CoreV1Api()
    api = client.ApiClient()
    pod = v1.read_namespaced_pod(name, namespace)
    return jsonify(api.sanitize_for_serialization(pod))

