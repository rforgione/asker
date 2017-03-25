from setpath import setpath
setpath()
from app.views import *
from app import db

class ViewThreadController(object):
    def __init__(self, thread_id):
        self.thread_id = thread_id

    def render_view(self):
        view = Views_ViewThread(self.thread_id)
        return view.render()
