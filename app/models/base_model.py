
class BaseModel:

    @staticmethod
    def get_doc(db, class_id, type):
        doc = db.get(type + "_" + class_id)
        print db
        return doc


