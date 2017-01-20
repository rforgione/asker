from app import db
from datetime import datetime

class Models_Answer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    create_date = db.Column(db.Integer)

    def __repr__(self):
        return '<Post %r>' % (self.content)
