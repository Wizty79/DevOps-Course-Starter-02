import pytest, requests, os
import mongomock
from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_find_one(self):
        collection = mongomock.MongoClient().db.collection
        obj = {'test_find_one': 'test_value'}
        collection.insert(obj)

        result_obj = self.hook.find(collection, {}, find_one=True)
        result_obj = {result: result_obj[result] for result in result_obj}
        self.assertEqual(obj, result_obj) 

