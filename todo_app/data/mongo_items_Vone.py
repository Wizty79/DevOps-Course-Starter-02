from flask import Flask, render_template, request
from azure.cosmos import cosmos_client #? possible solution
import json #? possible solution
import requests
import os
import certifi #? possible solution

def get_mongo_db():
    url = PRIMARY_CONNECTION_STRING_DB
    
    querystring = {
        "USERNAME":os.getenv("USERNAME"),
        "PASSWORD":os.getenv("PRIMARY_PASSWORD"),
        "HOST":os.getenv("HOST_DB"),
        "CORRELATIONID":os.getenv("CORRELATION_ID_DB")
    }

    response = requests.get(url, params=querystring)

    response_json = response.json()

    return response_json




# see link for suggestion https://stackoverflow.com/questions/44249604/how-to-read-data-from-azures-cosmosdb-in-python
