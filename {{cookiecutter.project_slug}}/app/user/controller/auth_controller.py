from flask import current_app, request
from flask_restplus import Resource

from app.common.base_resource import BaseResource
from app.common.errors import (ExpiredSignatureError, InvalidTokenError,
                               NotMatchOrUserDoesNotExistsError,
                               TokenBlackListedError)
from app.common.responses import ok, unauthorized
from app.user.decorators import token_required
from app.user.dto import AuthDto
from app.user.service.auth_service import login, logout

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class LoginResource(BaseResource):
    """
        User Login Resource
    """

    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        try:
            result = login(post_data)
            return result
        except NotMatchOrUserDoesNotExistsError as e:
            return unauthorized(e.message)


@api.route('/logout')
class LogoutResource(BaseResource):
    """
    Logout Resource
    """

    @api.doc('logout a user')
    @token_required
    def get(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        try:
            result = logout(auth_header)
            return ok(result, 'Logout successfully!')
        except InvalidTokenError:
            return unauthorized('Invalid token, please try to login again!')
        except ExpiredSignatureError:
            return unauthorized('Token is expired, please try to login again!')
        except TokenBlackListedError as e:
            return unauthorized(e.message)
