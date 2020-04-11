import datetime
import uuid

from app.common.errors import UserAlreadyExistError
from app.common.mixins import DictMixin
from app.user.model.user_model import User


def register_new_user(data):
    user = User.query.filter_by(email=data.get('email', None)).first() or \
            User.query.filter_by(username = data.get('username')).first()
    if not user:
        new_user = DictMixin.from_dict(User, data)
        new_user.public_id = str(uuid.uuid4())
        new_user.registered_on = datetime.datetime.utcnow()
        new_user.password = data.get('password')
        new_user.add()
    else:
        raise UserAlreadyExistError

def check_email_availability(data):
    user = User.query.filter_by(email=data.get('email', None)).first()
    return True if not user else False
