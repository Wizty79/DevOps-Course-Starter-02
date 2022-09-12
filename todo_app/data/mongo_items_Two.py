from flask import Flask, render_template, request
from azure.cosmos import cosmos_client #? possible solution
import json #? possible solution
import requests
import os
import certifi #? possible solution

def connect_mongo_db():
    
    
    client = pymongo.MongoClient(PRIMARY_CONNECTION_STRING_DB)
try:
    client.server_info() # validate connection string
except pymongo.errors.ServerSelectionTimeoutError:
    raise TimeoutError("Invalid API for MongoDB connection string or timed out when attempting to connect")


def create_mongo_todo_item():
    document_id = collection.insert_one({Item(card['id'], card['name'], list['name']}).inserted_id


def change_mongo_status():

    collection.update_one({"_id": document_id}, {"$set":{SAMPLE_FIELD_NAME: "Updated!"}})
    print("Updated document with _id {}: {}".format(document_id, collection.find_one({"_id": document_id})))


#all need to be adapted! How? 
