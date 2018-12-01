#/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *
from importlib import import_module
import os, sys, json
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_api import status
from config import app_name, bind_port, tasks_dir, data_dir

app = Flask(app_name)
CORS(app)

tasks = [f[:-3] for f in os.listdir(tasks_dir) if f.endswith(".py")]
sys.path.insert(0, tasks_dir)
python_version = sys.version_info[0]

@app.route('/<task>/<func>', methods=['GET', 'POST'])
def runTask(task, func):
    if task in tasks:
        module = import_module(task, tasks_dir)
        f = getattr(module, func)
        if python_version == 2:
            args = {k : v for k, v in request.args.iterlists()}
        else:
            args = {k : v for k, v in request.args.lists()}
        print(request.url, args)
        data = f(**args)
        #print(json.dumps(data))
        return json.dumps(data)
    else:
        return json.dumps("Task does not exist."), status.HTTP_404_NOT_FOUND

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=bind_port, threaded=False, debug=True)
