#!/usr/bin/env python
# coding=utf-8

import sys
import os

sys.path.append(os.path.join(os.path.abspath('.'), 'venv/Lib/site-packages'))

from credentials import TOKEN
from webapp2 import WSGIApplication, Route

routes = [
    Route('/' + TOKEN, handler='handlers.hook_handler.WebHookHandler:webhook_handler')
]
app = WSGIApplication(routes, debug=False)
