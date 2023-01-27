import unittest
from bson import ObjectId
from chalicelib.database.simple_base import Database


class TestDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.user = {'name': 'luis', 'value': 150}
        self.db = Database()
        return super().setUp()

    def tearDown(self) -> None:
        self.db.delete_many('user', {'name': 'luis'})
        return super().tearDown()

    def test_create(self):
        response = self.db.create('user', self.user)
        self.assertIsInstance(response, ObjectId)

    def test_get(self):
        self.db.create('user', self.user)
        response = self.db.get_object('user', {'name': 'luis'})
        self.assertAlmostEqual(len(response.keys()), len(self.user.keys()), 1)

    def test_update(self):
        edit_user = {'name': 'luis', 'value': 50}
        self.db.create('user', self.user)
        _ = self.db.update('user', {'name': 'luis'}, {'value': 50})
        response = self.db.get_object('user', {'name': 'luis'})
        assert len(response.keys()) - len(edit_user.keys()) == 1

    def test_delete(self):
        self.db.create('user', {'name': 'userDelete'})
        _ = self.db.delete('user', {'name': 'userDelete'})
        response = self.db.get_object('user', {'name': 'userDelete'})
        self.assertEqual(response, None)
