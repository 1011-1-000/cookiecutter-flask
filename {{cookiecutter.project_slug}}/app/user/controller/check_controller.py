from flask import request

from app.common.base_resource import BaseResource
from app.common.responses import ok
from app.user.dto import CheckDto
from app.user.service import user_service

api = CheckDto.api
_check = CheckDto.check

@api.route('/check')
class EmailCheckingResource(BaseResource):

    @api.doc('check wether email has been occupied (used for registered).')
    @api.expect(_check, validate=True)
    def post(self):
        data = request.json
        is_available = user_service.check_email_availability(data)
        res = {'is_available': is_available}
        msg = 'Email is available.' if is_available \
                                    else 'Email has been occupied.'
        return ok(res, msg)
