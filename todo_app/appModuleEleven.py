##ny app.py

from flask import Flask, render_template, request

from todo_app.flask_config import Config
import requests  
import os
from todo_app.data.item import Item
import todo_app.data.mongo_items_Vtwo as mongo_items_Vtwo
from todo_app.data.view_model import ViewModel
from flask.ext.login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app) #? 


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    
    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
            CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
            CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
            REDIRECT_URI = os.getenv("REDIRECT_URI")
            
            params = {
                "client_id": CLIENT_ID,
                "redirect_uri": REDIRECT_URI,
                "scope": "user"
            }
            
            # Add logic to redirect to the GitHub OAuth flow when unauthenticated
            # Request a user's GitHub identity
            # Need to return a redirect responce to the below URL, along with the correct query parameters 
            # parameters = client_id, redirect_uri?,allow_signup default is true,
            # (client_id=(os.getenv("Client_ID"), state='lkjbnvb546rfgh4764rtbm', allow_signup=flase)) 
            # GET https://github.com/login/oauth/authorize
            
            


    @login_manager.user_loader
    def load_user(user_id):
        pass # We will return to this later

    login_manager.init_app(app)

@app.route.login_required('/') #question syntax and indentation, why do this have to be further in but the other routes don't? 
def index():
    mongo_items = mongo_items_Vtwo.get_mongo_items()

    items = []

    for mongo_item in mongo_items: 
            item = Item.from_mongo_item(mongo_item)
            items.append(item)
    item_view_model = ViewModel(items)

    return render_template('index.html', view_model=item_view_model)
    
    @app.route.login_required('/create-todo', methods=['Post']) 
    def create_new_todo():

        response = mongo_items_Vtwo.create_mongo_todo_item()
        
        return index()


    @app.route.login_required('/update_status', methods=['POST']) 
    def update_status():
        
        response = mongo_items_Vtwo.change_mongo_status()

        return index()
    return app
 







