from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)
app.config.from_object('config')

from app.converters.client_converter import Client
app.url_map.converters['Client'] = Client

from app.routes import quiz
app.register_blueprint(quiz)
