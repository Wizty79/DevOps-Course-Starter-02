from flask import Flask, render_template, request
from azure.cosmos import cosmos_client #? possibly need
import json #? possibly need 
import requests
import os
import certifi #? possibly need

client = pymongo.MongoClient(PRIMARY_CONNECTION_STRING_DB)
db = client.chaostodo-db #my database name
document_id = todos.insert_one({Item(card['id'], card['name'], list['name'])}).inserted_id # replace card, but with what?
todos = db.ToDoItems #collection for todo items
dones = db.DoneItems #collection for done items

def connect_mongo_db():
    
    response = requests.get(client)

    response_json = response.json()

    return response_json


def create_mongo_todo_item():
    
    new_todo_title = request.form['todo-name']
        
    response = requests.request(client, document_id)


def change_mongo_status():
    
    card_id = request.form['todo-id']
    
    change_status = dones.update_one({"_id": document_id}, {"$set":{SAMPLE_FIELD_NAME: "Updated!"}}) 
    
    response = requests.request(client, change_status)

