from flask import Flask, render_template, request
from azure.cosmos import cosmos_client #? possible solution
import json #? possible solution
import requests
import os
import certifi #? possible solution

client = pymongo.MongoClient(PRIMARY_CONNECTION_STRING_DB)
db = client.chaostodo-db #my database name
todos = db.ToDoItems #collection for todo items
dones = db.DoneItems #collection for done items

def connect_mongo_db():
    client = pymongo.MongoClient(PRIMARY_CONNECTION_STRING_DB) #is this line need?
    
    response = requests.get(client)

    response_json = response.json()

    return response_json


def create_mongo_todo_item():
    document_id = collection.insert_one({Item(card['id'], card['name'], list['name'])}).inserted_id


def change_mongo_status():
    collection.update_one({"_id": document_id}, {"$set":{SAMPLE_FIELD_NAME: "Updated!"}})
    print("Updated document with _id {}: {}".format(document_id, collection.find_one({"_id": document_id})))



