from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='assets/templates/')
app.config.from_object('config')

app.config['OAUTH_CREDENTIALS'] = {
    'google': {
        'id': '953910222151-160q0nq4agchp1a6jpnflk07bunlke1j.apps.googleusercontent.com',
        'secret': 'KASEmNJ3vZw7EK18GnAB0cXv'
    }
}

db = SQLAlchemy(app)

from asker.models import *
from asker.views import *
from asker.controllers import *
from asker.routing import *
from asker.dbtools import *
