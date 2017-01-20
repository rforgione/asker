from asker import app
from asker.controllers import *
from asker.views import *

@app.route('/')
@app.route('/<name>')
def route_hello_world(name="Rob"):
    hwc = Controllers_HelloWorldController(name)
    return hwc.render_view()

@app.route('/api/name/<name>')
def route_set_name(name):
    api_name = API_Name()
    api_name.set_name(name)
    return None
