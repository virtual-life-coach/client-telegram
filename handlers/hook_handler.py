#!/usr/bin/env python
# coding=utf-8

from webapp2 import RequestHandler

import telegram
from message_handler import webhook
import json


class WebHookHandler(RequestHandler):
    def webhook_handler(self):
        # retrieve the JSON message and transform it into a Telegram object
        body = json.loads(self.request.body)
        update = telegram.Update.de_json(body)
        webhook(update)
