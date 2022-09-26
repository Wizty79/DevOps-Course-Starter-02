from flask import Flask, render_template, request
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests
import os

client = MongoClient(os.getenv("PRIMARY_CONNECTION_STRING_DB"))
db = client.chaostodoSaved
todos = db.ToDoItems

def get_mongo_items():
    
    return todos.find()

def create_mongo_todo_item():
    
    todos.insert_one({"name": request.form['todo-name'], "status": "To Do"})

def change_mongo_status():
    
    card_id = request.form['todo-id']
    
    change_status = todos.update_one({"_id": card_id}, {"$set":{"status": "Done"}}) 
    
