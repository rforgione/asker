from asker import db

class Models_User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255))
    nickname = db.Column(db.String(70))
    reputation = db.Column(db.Integer)
    questions = db.relationship('Models_Question', backref='author', lazy='dynamic')
    answers = db.relationship('Models_Answer', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)
