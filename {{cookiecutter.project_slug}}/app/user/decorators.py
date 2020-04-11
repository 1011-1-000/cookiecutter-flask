from functools import wraps

from flask import g, request

from app.common.errors import (ExpiredSignatureError, InvalidTokenError,
                               TokenBlackListedError, TokenMissedError)
from app.common.responses import unauthorized
from app.user.service.auth_service import current_user


def token_required(func):

    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            user_info = current_user(request)
            # save user information to flask g variable
            g.user = user_info
            # save the post or get request param to flask g variable
            post_data = request.json
            get_data = request.args
            g.args_post = post_data if post_data else {}
            g.args_get = get_data if get_data else {}
            return func(*args, **kwargs)
        except TokenMissedError as e:
            return unauthorized(e.message)
        except TokenBlackListedError as e:
            return unauthorized(e.message)
        except ExpiredSignatureError:
            return unauthorized('Token is expired, please try to login again!')
        except InvalidTokenError:
            return unauthorized('Invalid token, please try to login again!')

    return decorated
