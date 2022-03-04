from flask import Flask, render_template, request

from todo_app.flask_config import Config
import requests 
import os
from todo_app.data.item import Item
import todo_app.data.trello_items as trello_items

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    response_json = trello_items.get_trello_cards()

    items = []

    for trello_list in response_json:
        for card in trello_list['cards']:
            item = Item.from_trello_card(card, trello_list)
            items.append(item)

    return render_template('index.html', items = items)


@app.route('/create-todo', methods=['Post'])
def create_new_todo():
    new_todo_title = request.form['todo-name']

    response = trello_items.create_todo()
    
    print(response.text)

    return index()


@app.route('/update_status', methods=['POST'])
def update_status():
    
    card_id = request.form['todo-id']

    url = f"https://api.trello.com/1/cards/{card_id}"  

    querystring = {
            "key":os.getenv("API_KEY"),
            "token":os.getenv("API_TOKEN"),
            "idList":os.getenv("TRELLO_DONE_LIST_ID")
        }

    response = requests.request("PUT", url, params=querystring) 

    return index()
