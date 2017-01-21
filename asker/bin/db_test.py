from asker import db
from asker.models import *
from datetime import datetime

u = user.Models_User(email_address="john@gmail.com", nickname="John")

db.session.add(u)
db.session.commit()
