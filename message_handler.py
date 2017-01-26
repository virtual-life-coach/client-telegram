#!/usr/bin/env python
# coding=utf-8

import sys
import os

sys.path.append(os.path.join(os.path.abspath('.'), 'venv/Lib/site-packages'))

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler
from credentials import TOKEN
from handlers.handlers import error, help, start, list_activities, get_activity, update_activity, list_visits


def setup():
    bot = Bot(TOKEN)
    # update_queue is set to None. 0 workers are allowed on GAE, otherwise problems with multi-threading
    dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0)
    dispatcher.add_error_handler(error)
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("listactivities", list_activities))
    dispatcher.add_handler(CommandHandler("getactivity", get_activity, pass_args=True))
    dispatcher.add_handler(CommandHandler("updateactivity", update_activity, pass_args=True))
    dispatcher.add_handler(CommandHandler("listvisits", list_visits))
    return dispatcher


def webhook(update):
    dispatcher = setup()
    dispatcher.processUpdate(update)
