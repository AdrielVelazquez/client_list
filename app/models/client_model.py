import base_model
import connections


class ClientModel(base_model.BaseModel):
    type_name = "client"
    db = connections.get_clients_db()

    def __init__(self, class_id):
        '''
        The init accepts the class_id and then checks to see if the document exists
        Else the init will assign the name as None
        '''
        doc = self.get_doc(self.db, class_id, self.type_name)
        if doc:
            self.name = doc.get("name")
            self._id = doc.get("_id")
            self.exists = True

        else:
            self.name = None
            self.exists = False