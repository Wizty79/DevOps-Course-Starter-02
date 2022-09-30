import pytest, requests, os
import mongomock
import pymongo
from dotenv import load_dotenv, find_dotenv
from todo_app import app
from todo_app.data.mongo_items_Vtwo import create_mongo_todo_item

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_index_page(client):
    
    pymongo.MongoClient(client,'My test Task')

    response = client.get('/')
    
    response_html = response.data.decode()
    assert response.status_code == 200
    assert 'My test Task' in response_html
    
    
    
    