from os import environ
import uuid


class Config:
    HOST = environ.get('HOST', '127.0.0.1')
    PORT = environ.get('PORT', 8000)
    SECRET_KEY = uuid.uuid4().hex

    FLASKAPP = 'app.py'
    FLASK_DEBUG = False
