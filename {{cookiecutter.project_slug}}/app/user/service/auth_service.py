import datetime

import jwt
from flask import current_app

from app.common.errors import (ExpiredSignatureError, InvalidTokenError,
                               NotMatchOrUserDoesNotExistsError,
                               TokenBlackListedError, TokenMissedError)
from app.user.model.blacklist_model import BlackList
from app.user.model.user_model import User
from app.user.service.blacklist_service import add_token_to_blacklist
from config import SECRET_KEY


def login(data):
    user = User.query.filter_by(email=data.get('email')).first()
    if user and user.check_password(data.get('password')):
        token = generate_token(user.id)
        if token:
            result = {
                'message': 'Successfully logged in.',
                'Authorization': token.decode('utf-8'),
                'user_name': user.username
            }
            return result
    else:
        raise NotMatchOrUserDoesNotExistsError


def logout(authorization_header):
    token = authorization_header.split(" ")[1] if authorization_header else ''
    if token:
        resp = decode_token(token)
        if not isinstance(resp, str):
            add_token_to_blacklist(token=token)
    else:
        raise InvalidTokenError


def current_user(current_request):
    authorization_header = current_request.headers.get('Authorization')
    if authorization_header:
        token = authorization_header.split(" ")[1]
    else:
        raise TokenMissedError

    if token:
        user_id = decode_token(token)
        if not isinstance(user_id, str):
            user = User().get(user_id)
            data = {
                'user_id': user.id,
                'email': user.email,
                'admin': user.admin,
                'registered_on': str(user.registered_on)
            }
            return data
    else:
        raise InvalidTokenError


def generate_token(user_id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY)
        is_blacklisted_token = BlackList.check_blacklist(token)
        if is_blacklisted_token:
            raise TokenBlackListedError
        else:
            return payload['sub']
    except ExpiredSignatureError:
        raise ExpiredSignatureError
    except InvalidTokenError:
        raise InvalidTokenError
