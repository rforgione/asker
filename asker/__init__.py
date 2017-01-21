from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='assets/templates/')
app.config.from_object('config')
db = SQLAlchemy(app)

from asker.models import *
from asker.views import *
from asker.controllers import *
from asker.routing import *
from asker.dbtools import *
