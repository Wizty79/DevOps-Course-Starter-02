from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
import requests  
import os
from todo_app.data.item import Item
import todo_app.data.mongo_items_collect as mongo_items_collect
from todo_app.data.view_model import ViewModel
from flask_login import LoginManager, login_required, UserMixin
from urllib.parse import urlencode
import flask

class User(UserMixin):
        def __init__(self, id):
            self.id = id

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        redirect_url = f"https://github.com/login/oauth/authorize?client_id={os.getenv('GITHUB_CLIENT_ID')}"
        return redirect(redirect_url)


    @login_manager.user_loader
    def load_user(user_id):
        return user(user_id)

    login_manager.init_app(app)

    @app.route('/')
    @login_required
    def index():
        mongo_items = mongo_items_collect.get_mongo_items()

        items = []

        for mongo_item in mongo_items: 
                item = Item.from_mongo_item(mongo_item)
                items.append(item)
        item_view_model = ViewModel(items)

        return render_template('index.html', view_model=item_view_model)
    
    @app.route('/callback')
    def callback():
        authorisation_code = request.args['code']
        access_token_url = f"https://github.com/login/oauth/access_token"
        query_params = {
            "client_id": os.getenv('GITHUB_CLIENT_ID'),
            "client_secret": os.getenv('GITHUB_CLIENT_SECRET'),
            "code": authorisation_code
        }
        
        headers = {
            "Accept": "application/json"
        }
        
        access_token_response = request.post(access_token_url, parms = query_params, headers = headers)
    
        access_token = access_token_response.json()['access_token']
        
        user_info_url = "https://api.github.com/user"
        
        auth_headers = {
            "Authorization": f"Bearer {access_token}"
        }
    
        user_info_response = request.get(user_info_url, headares = auth_headers)
        
        user_id = user_info_response.json()['id']
        
        user = User(user_id)
        
        login_user(user)
        
        return redirect('/')

    @app.route('/create-todo', methods=['Post'])
    @login_required
    def create_new_todo():

        response = mongo_items_collect.create_mongo_todo_item()
        
        return index()


    @app.route('/update_status', methods=['POST'])
    @login_required
    def update_status():
        
        response = mongo_items_collect.change_mongo_status()

        return index()
    return app








