from flask import Flask, render_template, request
from todo_app.data.session_items import add_item, get_items

from todo_app.flask_config import Config
import requests 
import os

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():

    url = "https://api.trello.com/1/boards/6205664a19d7b437223061eb/lists"

    print(os.getenv("API_KEY"))

    querystring = {
        "key":os.getenv("API_KEY"),
        "token":os.getenv("API_TOKEN"),
        "cards": "open"
    }

    response = requests.request("GET", url, params=querystring)

    response_json = response.json()

    items = []

    for trello_list in response_json:
        for card in trello_list['cards']:
            card['status'] = trello_list['name']
            items.append(card)

    return render_template('index.html', items = items)

@app.route('/create-todo', methods=['Post'])
def create_new_todo():
    new_todo_title = request.form['todo-name']
    add_item(new_todo_title)
    return index()
