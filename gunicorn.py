#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from config import bind_port

bind = "0.0.0.0:{}".format(bind_port)
workers = 4
loglevel = "debug"
timeout = 60 * 10
limit_request_line = 0
