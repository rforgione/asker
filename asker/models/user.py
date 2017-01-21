from asker import db
from datetime import datetime

class Models_User(db.Model):
    # fields
    user_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255))
    nickname = db.Column(db.String(70))
    reputation = db.Column(db.Integer)
    create_date = db.Column(db.Integer)

    # relationships
    questions = db.relationship('Models_Question', backref='author', lazy='dynamic')
    answers = db.relationship('Models_Answer', backref='author', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Models_User, self).__init__(**kwargs)
        self.create_date = int(datetime.utcnow().strftime('%s'))
        self.reputation = 0

    def __repr__(self):
        return '<User %r>' % (self.nickname)
