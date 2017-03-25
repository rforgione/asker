from asker import db
from datetime import datetime

class Question(db.Model):
    # fields
    question_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    create_date = db.Column(db.Integer)

    # relationships
    answers = db.relationship('Answer', backref='question',
                              lazy='dynamic')

    def __init__(self, content, author):
        super(Question, self).__init__()
        self.create_date = int(datetime.utcnow().strftime('%s'))
        self.content = content
        self.author = author

    def __repr__(self):
        return '<Question %r>' % (self.content)
