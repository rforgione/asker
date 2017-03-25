from asker import app
from controllers.home_controller import HomeController
from asker.views import *

@app.route('/')
@app.route('/<string:name>')
def route_home(name="buddy"):
    hc = HomeController()
    return hc.render_view(name)

def route_view_question(question_id):
    pass

def route_post_question(user_id=None, content=None):
    pass
