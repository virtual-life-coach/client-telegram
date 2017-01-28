from google.appengine.api import urlfetch

import httplib
import json


endpoint = "https://vlc-server-process-centric.appspot.com/_ah/api/function/v1/"
headers = {
        "User-Agent":
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}


def get_activity_progress_req(activity_id):
    url_path = "activity/" + activity_id
    request = urlfetch.fetch(endpoint + url_path, headers=headers, method=urlfetch.GET)
    response = json.loads(request.content)
    return response


def list_activities_req(telegram_id):
    url_path = "activities/" + telegram_id
    request = urlfetch.fetch(endpoint + url_path, headers=headers, method=urlfetch.GET)
    response = json.loads(request.content)
    return response.get('items')


def list_appointments_req(telegram_id):
    url_path = "appointments/" + telegram_id
    request = urlfetch.fetch(endpoint + url_path, headers=headers, method=urlfetch.GET)
    response = json.loads(request.content)
    return response.get('items')


def update_activity_progress_req(activity_id, value):
    url_path = "activity/" + activity_id + "/" + value
    request = urlfetch.fetch(endpoint + url_path, headers=headers, method=urlfetch.PUT)
    return request.status_code == httplib.NO_CONTENT
