from asker import db

class Models_Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2000))
    user_id = db.Column(db.Integer, db.ForeignKey('models__user.user_id'))
    answers = db.relationship('Models_Answer', backref='question',
                              lazy='dynamic')

    def __repr__(self):
        return '<Question %r>' % (self.content)
