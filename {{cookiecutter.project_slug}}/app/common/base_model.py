from sqlalchemy.exc import SQLAlchemyError

from exts import db


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason


class BaseModel:

    def get(self, _id):
        return self.query.filter_by(id=_id).first()

    def add(self):
        db.session.add(self)
        return session_commit()

    def update(self):
        db.session.add(self)
        return session_commit()

    def delete(self):
        db.session.delete(self)
        return session_commit()

    def add_or_update(self):
        db.session.add(self)
        return session_commit()
