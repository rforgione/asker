from asker import db
from datetime import datetime

class Answer(db.Model):
    # fields
    answer_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.question_id'))
    create_date = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super(Answer, self).__init__(**kwargs)
        self.create_date = int(datetime.utcnow().strftime('%s'))

    def __repr__(self):
        return '<Post %r>' % (self.content)
