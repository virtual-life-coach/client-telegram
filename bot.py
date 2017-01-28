#!/usr/bin/env python
# coding=utf-8
import sys
import os

from telegram import Bot

sys.path.append(os.path.join(os.path.abspath("."), "venv/Lib/site-packages"))

from credentials import TOKEN
from webapp2 import WSGIApplication, Route, RequestHandler
import json


class SendHandler(RequestHandler):
    def send(self):
        params = json.loads(self.request.body)
        chat_id = str(params.get('chat_id'))
        message = str(params.get('message'))
        Bot(TOKEN).sendMessage(chat_id, message)

routes = [
    Route("/" + TOKEN, handler="handlers.hook_handler.WebHookHandler:webhook_handler"),
    Route("/send", handler="bot.SendHandler:send", methods=["POST"])
]
app = WSGIApplication(routes, debug=False)
