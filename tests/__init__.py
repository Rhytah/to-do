from todoapi.flask_app import app 
from todoapi.flask_models import User
import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client=app.test_client()
        self.req_data={
            "name":"Rita",
            "username":"Rhytah",
            "email":"somemail.com",
            "password":"secret"
        }

        self.task_data={
            "task_id":1,
            "title":"Sweep",
            "details":"Sweeping the house and compound"
        }


if __name__=='__main__':
    unittest.main()
