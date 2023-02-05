import os
from bson import ObjectId
from pymongo import MongoClient
from pymongo.cursor import Cursor


class Base:
    """Base simples de conexão com banco"""

    def __init__(self) -> None:
        self._client = None

    def inicializer(self):
        self._client = MongoClient(os.getenv('MONGO_URI'))

    @property
    def client(self):
        if self._client is None:
            self.inicializer()
        return self._client


class Database(Base):
    """Classe de interação com tabelas"""

    def __init__(self, db_name: str = 'adega') -> None:
        super().__init__()
        self._db = self.client[db_name]

    def get_object(self, table_name: str, query: dict) -> dict | None:
        return self._db[table_name].find_one(query)

    def get_objects(self, table_name: str, query: dict, order_by: list = None) -> Cursor | None:
        cursor = self._db[table_name].find(query)
        if order_by and cursor:
            cursor.sort(order_by)
        return cursor

    def create(self, table_name: str, object: dict) -> ObjectId:
        return self._db[table_name].insert_one(object).inserted_id

    def get_or_create(self, table_name: str, query: dict, obj_create: dict) -> dict | None:
        return self._db[table_name].find_one_and_update(query, {'$setOnInsert': obj_create}, upsert=True)

    def create_many(self, table_name: str, objects: list) -> list:
        return self._db[table_name].insert_many(objects).inserted_ids

    def update(self, table_name: str, query: dict, data: dict, upsert: bool = False) -> dict:
        return self._db[table_name].update_one(query, {'$set': data}, upsert).raw_result

    def update_many(self, table_name: str, query: dict, data: dict, upsert: bool = False) -> dict:
        return self._db[table_name].update_many(query, data, upsert).raw_result

    def delete(self, table_name: str, query: dict) -> dict:
        return self._db[table_name].delete_one(query).raw_result

    def delete_many(self, table_name: str, query: dict) -> dict:
        return self._db[table_name].delete_many(query).raw_result
