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
    #client = pymongo.MongoClient(PRIMARY_CONNECTION_STRING_DB) #is this line need?
    
    response = requests.get(client)

    response_json = response.json()

    return response_json


def create_mongo_todo_item():
    new_todo_title = request.form['todo-name']
    
    document_id = todos.insert_one({Item(card['id'], card['name'], list['name'])}).inserted_id 
    #move documnent_id out of function and into root of file? 
    
    response = requests.request(client, document_id)


def change_mongo_status():
    card_id = request.form['todo-id']
    
    collection = dones.update_one({"_id": document_id}, {"$set":{SAMPLE_FIELD_NAME: "Updated!"}})
    
    response = requests.request(client, collection)



