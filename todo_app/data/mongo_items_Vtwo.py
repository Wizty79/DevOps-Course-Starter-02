from flask import Flask, render_template, request
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests
import os

client = MongoClient(r"PRIMARY_CONNECTION_STRING_DB")
db = client.chaostodoSaved #my database name
todos = db.ToDoItems #collection for todo items
dones = db.DoneItems #collection for done items

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})

def connect_mongo_db():
    
    response = requests.get(client)

    response_json = response.json()

    return response_json


def create_mongo_todo_item():
    document_id = todos.insert_one({"_id": document_id}).inserted_id
    
    new_todo_title = request.form['todo-name']
        
    response = requests.request("POST", client, document_id)


def change_mongo_status():
    #document_id = dones.insert_one({"_id": document_id}).inserted_id
    
    card_id = request.form['todo-id']
    
    #change_status = dones.update_one({"_id": document_id}, {"$set":{SAMPLE_FIELD_NAME: "Updated!"}}) 
    change_status = dones.update_one(todos, update) #2 parameters needed, a filter to select correct item and and update directory
                                     
    response = requests.request("PUT", client, change_status)

