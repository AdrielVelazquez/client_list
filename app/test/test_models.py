import os
import unittest

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_PATH = ROOT_PATH + "/config_test.py"
os.environ["CLIENT_CONFIG"] = TEST_PATH

from app import app
from connections import get_clients_db
from app.models import client_model, base_model
import utils_unittest



class TestConverters(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not app.config['CLIENT_DB'].startswith("test"):
            print "YIKES THESE ARE NOT TEST DATABASES! EXITING!"
            exit()
        utils_unittest.setup_database(db_name=app.config['CLIENT_DB'])
        utils_unittest.load_generic_client__data(get_clients_db())

    @classmethod
    def tearDownClass(cls):
        utils_unittest.tear_down_database(db_name=app.config['CLIENT_DB'], delete=True)

    def testClientConverter(self):
        '''
        Testing the Client Converter Function
        '''

        #Testing the creation of a client
        for i in range(10):
            client = client_model.ClientModel(i)
            if i <= 4:
                self.assertEqual(client.name, "name_" + str(i))
                self.assertEqual(client._id,  "client_" + str(i))
                self.assertEqual(client.exists, True)
            else:
                self.assertEqual(client.name, None)
                self.assertEqual(client.exists, False)

    def testBaseModel(self):
        '''
        Testing the Static Methods in Base Function
        '''
        db = get_clients_db()
        for i in range(10):
            doc = base_model.BaseModel.get_doc(db, i, "client")
            if i <= 4:
                self. assertEqual(doc.get("name"), "name_" + str(i))
            else:
                self.assertEqual(doc, None)

        for i in range(10):
            doc = base_model.BaseModel.get_doc(db, i, "test")
            self.assertEqual(doc, None)


