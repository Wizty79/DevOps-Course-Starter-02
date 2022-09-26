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
        mongo_items = mongo_items.get_mongo_items()

        items = []

        for mongo_item in mongo_items: 
                item = Item.from_mongo_item(mongo_item)
                items.append(item)
        item_view_model = ViewModel(items)

        return render_template('index.html', view_model=item_view_model)
    
    @app.route('/create-todo', methods=['Post'])
    def create_new_todo():
    
        response = mongo_items_Vtwo.create_mongo_todo_item()
        
        return index()


    @app.route('/update_status', methods=['POST'])
    def update_status():
        
        response = mongo_items_Vtwo.change_mongo_status()

        return index()
    return app







