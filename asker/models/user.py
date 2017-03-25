from asker import db
from datetime import datetime

class User(db.Model):
    # fields
    user_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255))
    nickname = db.Column(db.String(70))
    reputation = db.Column(db.Integer)
    create_date = db.Column(db.Integer)

    # relationships
    questions = db.relationship('Question', backref='author', lazy='dynamic')
    answers = db.relationship('Answer', backref='author', lazy='dynamic')

    def __init__(self, email_address, nickname):
        super(User, self).__init__()
        self.create_date = int(datetime.utcnow().strftime('%s'))
        self.email_address = email_address
        self.nickname = nickname
        self.reputation = 0

    def __repr__(self):
        return '<User %r>' % (self.nickname)
