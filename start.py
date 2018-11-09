#!/usr/bin/env python
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

@app.route('/<task>', methods=['GET', 'POST'])
def runTask(task):
    if task in tasks:
        module = import_module(task, tasks_dir)
        func = getattr(module, 'func')
        args = {k : v for k, v in request.args.iterlists() if k != "token" }
        print(request.url, args)
        data = func(**args)
        #print(json.dumps(data))
        return json.dumps(data)
    else:
        return json.dumps(message="Task does not exist."), status.HTTP_404_NOT_FOUND

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=bind_port, threaded=False, debug=True)
