import unittest
from grocer import create_app, db
from grocer.models import User


class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_verification(self):
        user = User('testuser@test.com', 'password123')
        self.assertTrue(user.verify_password('password123'))
        self.assertFalse(user.verify_password('password'))

    def test_random_salts(self):
        user1 = User('testuser@test.com', 'password123')
        user2 = User('testuser2@test.com', 'password123')
        self.assertFalse(user1.password == user2.password)
