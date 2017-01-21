from asker import db

class Models_Question(db.Model):
    # fields
    question_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2000))
    user_id = db.Column(db.Integer, db.ForeignKey('models__user.user_id'))
    create_date = db.Column(db.Integer)

    # relationships
    answers = db.relationship('Models_Answer', backref='question',
                              lazy='dynamic')

    def __init__(self, **kwargs):
        super(Models_Question, self).__init__(**kwargs)
        self.create_date = int(datetime.utcnow().strftime('%s'))

    def __repr__(self):
        return '<Question %r>' % (self.content)
