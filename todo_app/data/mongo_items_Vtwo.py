from flask import Flask, render_template, request
from pymongo import MongoClient
import requests
import os

client = MongoClient(r"PRIMARY_CONNECTION_STRING_DB")
db = client.chaostododb #my database name
todos = db.ToDoItems #collection for todo items
dones = db.DoneItems #collection for done items

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
    change_status = dones.update_one(update) #2 parameters needed, a filter to select correct item and and update directory
                                     
    response = requests.request("PUT", client, change_status)

