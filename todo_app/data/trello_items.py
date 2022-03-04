import requests
import os

def get_trello_cards():
    url = "https://api.trello.com/1/boards/6205664a19d7b437223061eb/lists" 

    print(os.getenv("API_KEY"))

    querystring = {
        "key":os.getenv("API_KEY"),
        "token":os.getenv("API_TOKEN"),
        "cards": "open"
    }

    response = requests.request("GET", url, params=querystring)

    response_json = response.json()

    return response_json


def create_todo():
	url = "https://api.trello.com/1/cards"
	
	querystring = {
        "key":os.getenv("API_KEY"),
        "token":os.getenv("API_TOKEN"),
        "idList":os.getenv("TRELLO_TODO_LIST_ID"),
        "name": new_todo_title
    }

	response = requests.request("POST", url, params=querystring)

    