import unittest
from chalicelib.database.base_models import Model
from chalicelib.database.simple_base import Database

class TestModel(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.model = Model()
        self.test_data = {'name': 'Test', 'age': 30}

    def test_get(self):
        # Testa o método get com um query válido
        self.db.create(self.model.__table_name, self.test_data)
        result = self.model.get({'name': 'Test'})
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Test')
        self.assertEqual(result['age'], 30)

    def test_filter(self):
        # Testa o método filter com um query válido
        self.db.create(self.model.__table_name, self.test_data)
        result = self.model.filter({'age': 30})
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Test')
        self.assertEqual(result[0]['age'], 30)

    def test_get_or_create(self):
        # Testa o método get_or_create com um query válido
        result = self.model.get_or_create({'name': 'Test'}, self.test_data)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Test')
        self.assertEqual(result['age'], 30)

    def test_save(self):
        # Testa o método save com um objeto válido
        self.model.save(self.test_data)
        result = self.db.get_object(self.model.__table_name, {'name': 'Test'})
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Test')
        self.assertEqual(result['age'], 30)

    def test_update(self):
        # Testa o método update com um query válido
        self.db.create(self.model.__table_name, self.test_data)
        self.model.update({'name': 'Test'}, {'age': 35})
        result = self.db.get_object(self.model.__table_name, {'name': 'Test'})
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Test')
        self.assertEqual(result['age'], 35)

    def test_delete(self):
        self.db.create(self.model.__table_name, self.test_data)
        self.model.delete({'name': 'Test'}, many=True)
        result = self.db.get_object(self.model.__table_name, {'name': 'Test'})
        self.assertIsNone(result)