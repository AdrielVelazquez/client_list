import connections


class BaseModel:

    @staticmethod
    def get_doc(db, class_id, type):
        doc = db.get(type + "_" + class_id)
        return doc


