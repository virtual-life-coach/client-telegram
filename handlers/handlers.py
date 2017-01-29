# coding=utf-8

from functools import partial
from message_handler import logger
from request import get_activity_progress_req, list_activities_req, list_appointments_req, update_activity_progress_req


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def help(bot, update):
    bot.sendMessage(update.message.chat_id, "Type '/' to list the available commands!")


def start(bot, update):
    bot.sendMessage(update.message.chat_id,
                    "Hi! I will be your Coach! We will achieve extraordinary successes together!\n" +
                    "Type '/' to list the available commands!")


def list_activities(bot, update):
    chat_id = update.message.chat_id
    api_call = partial(list_activities_req, str(chat_id))

    def success(result):
        if result:
            content = "This is the list of your activities. Hold on!\n"
            content += "\n".join(map(lambda a: repr_activity(a), result))
            bot.sendMessage(chat_id, content)
        else:
            bot.sendMessage(chat_id, "You have completed all the activities: I am so proud of you. "
                                     "Wait tomorrow for a new one!")

    execute_request(api_call, success, partial(send_failure_message, bot, chat_id))


def get_activity_progress(bot, update, args):
    # args[0] should be the activity id
    chat_id = update.message.chat_id
    try:
        api_call = partial(get_activity_progress_req, args[0])

        def success(result):
            bot.sendMessage(chat_id, repr_activity(result))

        execute_request(api_call, success, partial(send_failure_message, bot, chat_id))
    except (IndexError, ValueError):
        bot.sendMessage(chat_id, "Usage:\n/getactivity activityId")


def update_activity(bot, update, args):
    # args[0] should be the activity id
    # args[1] should be the new activity value
    chat_id = update.message.chat_id
    try:
        api_call = partial(update_activity_progress_req, args[0], args[1])

        def success(result):
            if result:
                bot.sendMessage(chat_id, "Activity successfully updated.")
            else:
                bot.sendMessage(chat_id, "Unable to update activity.")

        execute_request(api_call, success, partial(send_failure_message, bot, chat_id))
    except (IndexError, ValueError):
        bot.sendMessage(chat_id, "Usage:\n/updateactivity activityId newValue")


def list_appointments(bot, update):
    chat_id = update.message.chat_id
    api_call = partial(list_appointments_req, str(chat_id))

    def success(result):
        if result:
            content = "This is the list of your future appointments!\n"
            content += "\n".join(map(lambda a: repr_appointment(a), result))
            bot.sendMessage(chat_id, content)
        else:
            bot.sendMessage(chat_id, "You have no appointment scheduled.")

    execute_request(api_call, success, partial(send_failure_message, bot, chat_id))


def execute_request(api_call, on_success, on_failure):
    logger.info("Executing request: " + str(api_call.func))
    try:
        result = api_call()
        logger.info("Response: " + str(result))
        on_success(result)
    except Exception as e:
        logger.warning("Error while executing request: " + e.message)
        on_failure(e.message)


def send_failure_message(bot, chat_id, error_message):
    bot.sendMessage(chat_id, "An error occurred while executing request: " + error_message)


def repr_activity(activity):
    return "Id: " + str(activity.get("id")) + \
           "\nTask: " + activity.get("details") + \
           "\nDeadline: " + activity.get("deadlineDate") + \
           "\nTarget value: " + activity.get("targetValue") + \
           "\nCurrent value: " + activity.get("currentValue") + \
           "\nCompleted: " + str(activity.get("completed"))


def repr_appointment(appointment):
    return "Doctor id: " + str(appointment.get("doctorId")) + \
           "\nDate: " + appointment.get("date") + \
           "\nLocation: " + appointment.get("location")
