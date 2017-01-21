import sys
import os
sys.path.append(os.realpath.)
from app.views import *
from app import db

class Controllers_ViewQuestionController(object):
    def __init__(self, question_id):
        self.thread_id = thread_id

    def render_view(self):
        view = Views_ViewThread(self.thread_id)
        return view.render()
