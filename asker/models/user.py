from app import db

class Models_User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255))
    nickname = db.Column(db.String(70))
    reputation = db.Column(db.Integer)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)
