from ..views import *
from ..models.question import *
from sqlalchemy import desc

class HomeController(object):
    def __init__(self):
        pass

    def render_view(self, name):
        top_5 = self.get_threads()
        view = HomeView(name, top_5)
        return view.render()

    def get_threads(self):
        return Question.query.order_by(desc(Question.create_date)).limit(5)



