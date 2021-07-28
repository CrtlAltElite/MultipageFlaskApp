import os
class Config():
    REGISTERED_USERS = {
        'kevinb@codingtemple.com':{"name":"Kevin","password":"abc123"},
        'johnl@codingtemple.com':{"name":"John", "password":"Colt45"},
        'joelc@codingtemple.com':{"name":"Joel","password":"MorphinTime"}
    }
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
