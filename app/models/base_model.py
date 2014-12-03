
class BaseModel:

    @staticmethod
    def get_doc(db, class_id, type):
        '''
        :param db: database object
        :param class_id: is the hash id for any specific object
        :param type: type is the doc_type of the doc/class
        :return: a database object from couchdb
        '''
        doc = db.get(type + "_" + str(class_id))
        return doc


