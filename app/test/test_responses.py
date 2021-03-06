import os
import unittest

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_PATH = ROOT_PATH + "/config_test.py"
os.environ["CLIENT_CONFIG"] = TEST_PATH

from app import app
from connections import get_clients_db
import utils_unittest



class TestResponses(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not app.config['CLIENT_DB'].startswith("test"):
            print "YIKES THESE ARE NOT TEST DATABASES! EXITING!"
            exit()
        utils_unittest.setup_database(db_name=app.config['CLIENT_DB'])
        utils_unittest.load_generic_client__data(get_clients_db())


    @classmethod
    def tearDownClass(cls):
        print "ApiSigninTestCase: tear down"
        utils_unittest.tear_down_database(db_name=app.config['CLIENT_DB'], delete=True)


    def testAccurateData(self):
        '''
        Testing the data is built properly.
        '''
        db = get_clients_db()
        print db
        for idx, doc in enumerate(db):
            self.assertEqual(doc, "client_" + str(idx))

    def testEndpoint(self):
        '''
        Testing the responses from the endpoint
        '''
        self.app = app.test_client()
        response = self.app.get('/api/client/0', content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, '{"client": "name_0", "Exists": true}')

        # Test Bad input
        response = self.app.get('/api/client/ZZZ', content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data, '{"client": null, "Exists": false}')