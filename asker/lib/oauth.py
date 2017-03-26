from asker import app
from flask import request, url_for
from oauth2client.client import OAuth2WebServerFlow
from flask import redirect
import httplib2
from apiclient.discovery import build

class OAuthSignIn(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    def authorize(self):
        pass

    def callback(self):
        pass


    def get_callback_url(self):
        return url_for('oaut_callback', provider=self.provider_name, _external=True)

    @classmethod
    def get_provider(cls, provider_name):
        if cls.providers is None:
            cls.providers = {}
            for provider_class in cls.__subclasses__():
                provider = provider_class()
                cls.providers[provider.provider_name] = provider
        return cls.providers[provider_name]

class GoogleSignIn(OAuthSignIn):
    def __init__(self):
        super(GoogleSignIn, self).__init__('google')
        self.flow = OAuth2WebServerFlow(client_id=self.consumer_id,
                                        client_secret=self.consumer_secret,
                                        scope='https://www.googleapis.com/auth/userinfo.email',
                                        redirect_uri='http://localhost:5000/oauth2callback')

    def authorize(self):
        auth_uri = self.flow.step1_get_authorize_url()
        return redirect(auth_uri, code=302)

    def callback(self):
        if 'code' not in request.args:
            return None, None, None
        credentials = self.flow.step2_exchange(request.args['code'])
        http = credentials.authorize(httplib2.Http())
        service = build('oauth2', 'v2', http=http)
        data = service.userinfo().get().execute()
        email, id, nickname = data['email'], data['id'], data['given_name']
        # TODO: load user into Users table


