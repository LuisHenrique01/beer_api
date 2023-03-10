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

    @classmethod
    def get_table_name(cls) -> None:
        try:
            return cls.Meta.table_name
        except AttributeError:
            return cls.__class__.__name__

    @classmethod
    def get(cls, query: dict = None, **kwargs):
        query = query or kwargs
        return cls.from_dict(cls.__db.get_object(cls.get_table_name(), query))

    @classmethod
    def filter(cls, query: dict = None, order_by: list = None, page: int = None, limit: int = None, **kwargs):
        query = query or kwargs
        return cls.__db.get_objects(cls.get_table_name(), query, order_by, page, limit)

    @classmethod
    def get_or_create(cls, query: dict = None, obj_create: dict = None, **kwargs):
        query = query or kwargs
        return cls.from_dict(cls.__db.get_or_create(cls.get_table_name(), query, obj_create))

    @classmethod
    def save_many(cls, objects: list = None):
        return cls.__db.create_many(cls.get_table_name(), [obj if isinstance(obj, dict) else obj.to_dict()
                                    for obj in objects])

    def save(self):
        return self.__db.create(self.get_table_name(), self.to_dict())

    def update(self, query: dict = None, data: dict = None, upsert: bool = False, many: bool = False, **kwargs):
        data = data or kwargs or {'_id': self._id}
        if many:
            return self.__db.update_many(self.get_table_name(), query, data, upsert)
        return self.__db.update(self.get_table_name(), query, data, upsert)

    def delete(self, query: dict = None, many: bool = False, **kwargs):
        query = query or kwargs or {'_id': self._id}
        if many:
            return self.__db.delete_many(self.get_table_name(), query)
        return self.__db.delete(self.get_table_name(), query)
    
    @classmethod
    def count_documents(cls, query: dict = {}):
        return  cls.__db.coun_documents(cls.get_table_name(), query)

    def to_dict(self):
        obj = vars(self)
        return obj
    
    @classmethod
    def from_dict(cls, data: dict):
        if data:
            _id = data.pop('_id', None)
            obj = cls(**data)
            if _id:
                obj._id = _id
            return obj
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict())
