from asker import app
from controllers.home_controller import HomeController
from asker.lib.oauth import OAuthSignIn
from flask_login import current_user

@app.route('/')
@app.route('/<string:name>')
def route_home(name="buddy"):
    hc = HomeController()
    return hc.render_view(name)

@app.route('/oauth2callback')
def route_callback():
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider('google')
    social_id, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed!')
        redirect(url_for('/'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('/'))


def route_view_question(question_id):
    pass

def route_post_question(user_id=None, content=None):
    pass
