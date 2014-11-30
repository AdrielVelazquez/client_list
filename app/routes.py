from flask import Blueprint

quiz = Blueprint('api', __name__, url_prefix='/api')


@quiz.route("/client/<Client:client>", methods=['GET'])
def get_client(client):
    '''
    Get client information
    '''
    return {"client": client.name, "Exists": client.exists}