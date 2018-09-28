from todoapi.flask_models import User,Task
from tests import BaseTestCase
import unittest
import json

class UserTestCase(BaseTestCase):

    def test_register_a_user(self):
        test_user={
            'name':'Rita',
            'username':'Rhytah',
            'email':'somemail.com',
            'password':'secret'
        }
        response = self.test_client.post(
            '/register', data=json.dumps(test_user),content_type='application/json'
        )
        self.assertEqual(response.status_code,201)
        self.assertIn("Rhytah you have successfully created your account", str(response.data))

    def test_login(self):
        test_user={
            'username':'Rhytah',
            'password':'secret'
        }
        response=self.test_client.post(
            '/login',data=json.dumps(test_user), content_type='application/json')
        self.assertIn("Rhytah you have logged in", str(response.data))

    def test_fetch_users_none(self):
        test_users={}
        response= self.test_client.get(
            '/users',data=json.dumps(test_users),content_type='application/json'
        )
        self.assertEqual(response.status_code,404)
        self.assertIn("There are no registered users", str(response.data))

    def test_fetch_users(self):
        test_users=[{
        'name':'Rita',
        'username':'Rhytah',
        'email':'somemail.com',
        'password':'secret'
        },
        {
        'name':"Fatuma",
        'username':'fatty',
        'email':'fatty@mail.com',
        'password':'something'
        }]
        response= self.test_client.get(
            '/users',data=json.dumps(test_users),content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        self.assertIn("There are the registered users", str(response.data))

class TasksTestCase(BaseTestCase):
    def test_create_a_task(self):
        response= self.test_client.post(
            '/tasks', data=json.dumps(self.task_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,201)
        self.assertIn("You have created task", str(response.data))


