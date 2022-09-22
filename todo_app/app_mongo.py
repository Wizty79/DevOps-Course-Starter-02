from flask import Flask, render_template, request

from todo_app.flask_config import Config
import requests  
import os
from todo_app.data.item import Item
import todo_app.data.mongo_items_Vtwo as mongo_items
from todo_app.data.view_model import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    
    @app.route('/')
    def index():
        response_json = mongo_items.connect_mongo_db()

        items = []

        item_view_model = ViewModel(items)

        for trello_list in response_json: # replace with _id? or document_id?
            for card in trello_list['cards']:
                item = Item.from_trello_card(card, trello_list)
                items.append(item)

        return render_template('index.html', view_model=item_view_model)
    
    @app.route('/create-todo', methods=['Post'])
    def create_new_todo():
    
        response = mongo_items_Vtwo.connect_mongo_db()
        
        return index()


    @app.route('/update_status', methods=['POST'])
    def update_status():
        
        response = mongo_items_Vtwo.change_mongo_status()

        return index()
    return app







