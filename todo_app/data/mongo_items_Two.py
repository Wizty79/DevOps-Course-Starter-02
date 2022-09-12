from flask import Flask, render_template, request
from azure.cosmos import cosmos_client #? possible solution
import json #? possible solution
import requests
import os
import certifi #? possible solution

def get_mongo_db():
    
    
    client = pymongo.MongoClient(PRIMARY_CONNECTION_STRING_DB)
try:
    client.server_info() # validate connection string
except pymongo.errors.ServerSelectionTimeoutError:
    raise TimeoutError("Invalid API for MongoDB connection string or timed out when attempting to connect")