import datetime

from app.common.base_model import BaseModel
from exts import db


class BlackList(db.Model, BaseModel):
    __tablename__ = 'blacklist'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(512), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.utcnow()

    def __repr__(self):
        return f'<id: token: {self.token}'

    @staticmethod
    def check_blacklist(token):
        res = BlackList.query.filter_by(token=str(token)).first()
        return True if res else False
