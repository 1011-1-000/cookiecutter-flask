import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'db/dev.sqlite')
SECRET_KEY = os.environ.get(
    'SECRET_KEY') or 'd*eds-w234d-2d2lq-#$dw3-@hjde'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
