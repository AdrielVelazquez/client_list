from werkzeug.routing import BaseConverter


class Client(BaseConverter):

    def to_python(self, value):
        return value