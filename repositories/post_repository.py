from pymongo import MongoClient, DESCENDING

from infrastructure import EnvironmentManager
from models import Post


class PostRepository():
    def __init__(self):
        environment_manager = EnvironmentManager()

        host = environment_manager.get('DB_HOST')
        username = environment_manager.get('DB_USER')
        password = environment_manager.get('DB_PASSWORD')
        database_name = environment_manager.get('DB_NAME')

        url = f'mongodb://{host}:27017'
        if username != '':
            creds = f'{username}:{password}@'
            url = f'mongodb://{creds}{host}:27017'

        client = MongoClient(url)
        db = client[database_name]
        self.collection = db.post

    def insert_one(self, object_to_db):
        result = self.collection.insert_one(object_to_db.to_doc())
        return result.inserted_id

    def find_one(self, find_attrs):
        from_db = self.collection.find_one(find_attrs)
        if from_db is not None:
            from_db = Post(from_db)
        return from_db

    def find(self, find_attrs, **kwargs):
        from_db = self.collection.find(find_attrs, **kwargs).sort('$natural',
                                                                  DESCENDING)
        if from_db is not None:
            from_db = [Post(attrs) for attrs in from_db]
        return from_db
