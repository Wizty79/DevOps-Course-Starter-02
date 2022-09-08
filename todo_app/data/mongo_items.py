from flask import Flask, render_template, request
from azure.cosmos import cosmos_client #? possible solution
import json #? possible solution
import requests
import os

def get_mongo_db():
    url = PRIMARY_CONNECTION_STRING_DB
    
    querystring = {
        "USERNAME":os.getenv("USERNAME"),
        "PASSWORD":os.getenv("PRIMARY_PASSWORD"),
        "HOST":os.getenv("HOST_DB"),
        "CORRELATIONID":os.getenv("CORRELATION_ID_DB")
    }

