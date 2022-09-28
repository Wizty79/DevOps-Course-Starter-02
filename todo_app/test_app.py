import pytest, requests, os
import mongomock
from dotenv import load_dotenv, find_dotenv
from todo_app import app
from todo_app.data.mongo_items_Vtwo import create_new_todo

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

@mongomock
def test_index_page(client):
    
    create_new_todo('My test Task')
    
    response = client.get('/')
    
    response_html = response.data.decode()
    assert 'My test Task' in response_html
    
    
    
    