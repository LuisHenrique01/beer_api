import json
from .simple_base import Database


class BaseModelABS:

    def from_dict(self, data: dict):
        raise NotImplementedError("O método de conversão precisa ser implementado")

    def to_dict(self):
        raise NotImplementedError("O método de conversão precisa ser implementado")

    class Meta:
        ...


class Model(BaseModelABS):

    __db = Database()
    __table_name = None

    def set_table_name(self) -> None:
        try:
            if not self.__table_name:
                self.__table_name = self.Meta.table_name
        except AttributeError:
            self.__table_name = self.__class__.__name__

    def get(self, query: dict = None, **kwargs):
        self.set_table_name()
        query = query or kwargs
        return self.__db.get_object(self.__table_name, query)

    def filter(self, query: dict = None, order_by: list = None, **kwargs):
        self.set_table_name()
        query = query or kwargs
        return self.__db.get_objects(self.__table_name, query, order_by)

    def get_or_create(self, query: dict = None, obj_create: dict = None, **kwargs):
        self.set_table_name()
        query = query or kwargs
        obj_create = obj_create or self.to_dict()
        return self.__db.get_or_create(self.__table_name, query, obj_create)

    def save(self, objects: list = None, many: bool = False):
        self.set_table_name()
        if many:
            return self.__db.create_many(self.__table_name, [obj if isinstance(obj, dict) else obj.to_dict()
                                                             for obj in objects])
        return self.__db.create(self.__table_name, self.to_dict())

    def update(self, query: dict, data: dict = None, upsert: bool = None, many: bool = None, **kwargs):
        self.set_table_name()
        data = data or kwargs
        if many:
            return self.__db.update_many(self.__table_name, query, data, upsert)
        return self.__db.update(self.__table_name, query, data, upsert)

    def delete(self, query: dict = None, many: bool = None, **kwargs):
        self.set_table_name()
        query = query or kwargs
        if many:
            return self.__db.delete_many(self.__table_name, query)
        return self.__db.delete(self.__table_name, query)

    def to_dict(self):
        return vars(self)
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict())
