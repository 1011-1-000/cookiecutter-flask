import json

from tests.utils.rest import RestMixin


def register(client):
    with client:
        user_data = json.dumps(dict(
            email='example@gmail.com',
            username='username',
            password='123456',
            public_id='ctr'
        ))

        result = RestMixin.post(client, '/user/', user_data)
    return result


def login(client):
    with client:
        user_data = json.dumps(dict(
            email='example@gmail.com',
            password='123456',
        ))
    result = RestMixin.post(client, '/auth/login', user_data)
    return result
