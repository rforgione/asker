from flask import render_template

class HomeView(object):
    TEMPLATE = 'hello_world.html'

    def __init__(self, name, top_5):
        self.name = name
        self.top_5 = top_5

    def render(self):
        template_vars = {
            "name": self.name,
            "top_5": self.top_5
        }
        return render_template(self.TEMPLATE, **template_vars)
