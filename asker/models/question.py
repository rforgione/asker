from app import db

class Model_Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2000))
    answers = db.relationship('Answer', backref='question', lazy='dynamic')

    def __repr__(self):
        return '<Question %r>' % (self.content)
