import os
import unittest

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_PATH = ROOT_PATH + "/config_test.py"
os.environ["CLIENT_CONFIG"] = TEST_PATH

from app import app
from connections import get_clients_db
from app.converters import client_converter
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
        for i in range(5):
            client = client_converter.Client(i)
            client_object = client.to_python(i)
            self.assertEqual(client_object.name, "name_" + str(i))