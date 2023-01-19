from flask import Flask, render_template, request
import pymongo
from bson.objectid import ObjectId
import requests
import os

import logging
from flask import current_app as app

from loggly.handlers import HTTPSHandler
from logging import Formatter


def mongo_connect():
    client = pymongo.MongoClient(os.getenv("PRIMARY_CONNECTION_STRING_DB"))
    db = client.chaostodoSaved
    todos = db.ToDoItems
    #app.logger.info("Value of mongo_connect is %s", mongo_connect())
    
    return todos

def get_mongo_items():
    todos = mongo_connect()
    
    return todos.find()

def create_mongo_todo_item():
    todos = mongo_connect()
    
    todos.insert_one({"name": request.form['todo-name'], "status": "To Do"})
    #app.logger.info("Value of create_mongo_todo_items is %s", create_mongo_todo_item())
    app.logger.info("Value of new item is %s", todos.insert_one) #working?

def change_mongo_status():
    todos = mongo_connect()
    
    mongo_id = request.form['todo-id']
    
    change_status = todos.update_one({"_id": mongo_id}, {"$set":{"status": "Done"}}) 
    app.logger.info("Status change to done for todo with id %s", mongo_id)
