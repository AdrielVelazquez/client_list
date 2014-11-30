from werkzeug.routing import BaseConverter
from app.models import client_model


class Client(BaseConverter):

    def to_python(self, value):
        '''

        :param value:
        :return: the class Client Model with the Client Document
        '''
        return client_model.ClientModel(value)