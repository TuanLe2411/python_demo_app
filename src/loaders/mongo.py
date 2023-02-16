import os
from pymongo import MongoClient


class MongoDb:
    _db: MongoClient

    def loader(self):
        _connection_string = os.environ.get("MONGO_URL")
        self._db = MongoClient(_connection_string)
        pass

    @property
    def context(self) -> MongoClient:
        _db_name = os.environ.get("MONGO_DB_NAME")
        return self._db[_db_name]
        pass


mongo_db = MongoDb()
