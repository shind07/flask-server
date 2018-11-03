#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

with open("config.json") as f:
    j = json.load(f)
    app_name = j["name"]
    bind_port = j["port"]
    tasks_dir = j["tasks"]
    data_dir = j["data"]
