import json
from server_db import User


def login_user(**kwargs):
    user = User()
    response = user.connect_user(**kwargs)
    if response is not None:
        return response


def action_request(kwargs):
    for key, i in kwargs.items():
        if key == 'login':
            response = login_user(**i)
            if response is not None:
                return response, True
