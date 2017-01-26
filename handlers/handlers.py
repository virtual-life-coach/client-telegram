# coding=utf-8

from message_handler import logger


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def help(bot, update):
    bot.sendMessage(update.message.chat_id, "Type '/' to list the available commands!")


def start(bot, update):
    bot.sendMessage(update.message.chat_id,
                    "Hi! I will be your Coach! We will achieve extraordinary successes together!\n" +
                    "Type '/' to list the available commands!")


def list_activities(bot, update):
    bot.sendMessage(update.message.chat_id, "Empty list")


def get_activity(bot, update, args):
    # args[0] should be the activity id
    chat_id = update.message.chat_id
    try:
        activity_id = int(args[0])
        bot.sendMessage(chat_id, "Received " + args[0])
    except (IndexError, ValueError):
        bot.sendMessage(chat_id, "Usage:\n/getactivity activityId")


def update_activity(bot, update, args):
    # args[0] should be the activity id
    # args[1] should be the new activity value
    chat_id = update.message.chat_id
    try:
        activity_id = int(args[0])
        activity_value = int(args[1])
        bot.sendMessage(chat_id, "Received " + args[0] + " " + args[1])
    except (IndexError, ValueError):
        bot.sendMessage(chat_id, "Usage:\n/updateactivity activityId newValue")


def list_visits(bot, update):
    bot.sendMessage(update.message.chat_id, "Empty list")
