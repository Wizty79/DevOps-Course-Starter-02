from flask import Flask, render_template, request
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests
import os

client = MongoClient(os.getenv("PRIMARY_CONNECTION_STRING_DB"))
db = client.chaostodoSaved #my database name
todos = db.ToDoItems #collection for todo items
#ones = db.DoneItems #collection for done items

#A common task in web applications is to get an ObjectId from the request URL and find the matching document. 
#It’s necessary in this case to convert the ObjectId from a string before passing it to find_one:
#The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})

def get_mongo_items():
    
    return todos.find()

def create_mongo_todo_item():
    
    todos.insert_one({"name": request.form['todo-name'], "status": "To Do"})

def change_mongo_status():
    #document_id = dones.insert_one({"_id": document_id}).inserted_id
    
    card_id = request.form['todo-id']
    
    change_status = todos.update_one({"_id": card_id}, {"$set":{"status": "Done"}}) 
    
