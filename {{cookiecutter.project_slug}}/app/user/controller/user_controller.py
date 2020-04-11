from flask import request
from flask_restplus import Resource

from app.common.base_resource import BaseResource
from app.common.errors import UserAlreadyExistError
from app.common.responses import bad_request, created, ok
from app.user.dto import UserDto
from app.user.service import user_service

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UsersResource(BaseResource):

    @api.response(201, 'User successfully created.')
    @api.doc('create new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        try:
            user_service.register_new_user(data)
            return created('Successfully registered!')
        except UserAlreadyExistError as e:
            return bad_request(e.message)

    def get(self):
        dic = {
            'data': 'test'
        }
        return ok(dic, 'test')
