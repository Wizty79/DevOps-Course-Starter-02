from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
import requests
import os
from todo_app.data.item import Item
import todo_app.data.mongo_items_collect as mongo_items_collect
from todo_app.data.view_model import ViewModel
from flask_login import LoginManager, login_required, UserMixin, login_user, current_user
import flask
from functools import wraps

import logging
from loggly.handlers import HTTPSHandler
from logging import Formatter

class User(UserMixin):
        def __init__(self, id):
            role = ["read","write"]
            self.id = id
            if self.id == "94174586":
                self.role = "write"
            else:
                self.role = "read"
 
def check_user_role(func):
    @wraps(func)
    def inner_check():
        if os.getenv('LOGIN_DISABLED') == 'True' or current_user.role == "write":
            return func()
        else:
            return "unauthorized user"
    return inner_check

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.config['LOGIN_DISABLED'] = os.getenv('LOGIN_DISABLED') == 'True'
    
    login_manager = LoginManager()
    
    if app.config['LOGGLY_TOKEN'] is not None:
        handler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{app.config["LOGGLY_TOKEN"]}/tag/todo_app')
        handler.setFormatter(
            Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
        )
        app.logger.addHandler(handler)
        
        #app.logger.info("Value of role is %s", role)
        #app.logger.info("Value of login_manager is %s", login_manager)
        #app.logger.info("Value of unauthenticated is %s", unauthenticated())
        #app.logger.info("Value of items is %s", items)
        #app.logger.info("Value of user is $s", User(id))

    @login_manager.unauthorized_handler
    def unauthenticated():
        redirect_url = f"https://github.com/login/oauth/authorize?client_id={os.getenv('GITHUB_TERRA_CLIENT_ID')}"
        return redirect(redirect_url)


    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)

    login_manager.init_app(app)

    @app.route('/')
    @login_required
    def index():
        mongo_items = mongo_items_collect.get_mongo_items() # rename!

        items = []

        for mongo_item in mongo_items: 
                item = Item.from_mongo_item(mongo_item)
                items.append(item)
        item_view_model = ViewModel(items)
        user_role = "write" if os.getenv('LOGIN_DISABLED') == 'True' else current_user.role

        return render_template('index.html', view_model=item_view_model, chaos_user = user_role)

    
    @app.route('/callback')
    def callback():
        authorisation_code = request.args['code']
        access_token_url = f"https://github.com/login/oauth/access_token"
        query_params = {
            "client_id": os.getenv('GITHUB_TERRA_CLIENT_ID'),
            "client_secret": os.getenv('GITHUB_TERRA_CLIENT_SECRET'),
            "code": authorisation_code
        }
        
        headers = {
            "Accept": "application/json"
        }
        
        access_token_response = requests.post(access_token_url, params = query_params, headers = headers)
    
        access_token = access_token_response.json()['access_token']
        
        user_info_url = "https://api.github.com/user"
        
        auth_headers = {
            "Authorization": f"Bearer {access_token}"
        }
    
        user_info_response = requests.get(user_info_url, headers = auth_headers)
        
        user_id = user_info_response.json()['id']
        
        user = User(user_id)
        
        login_user(user)
        
        return redirect('/')

    @app.route('/create-todo', methods=['Post'])
    @login_required
    @check_user_role
    def create_new_todo():

        response = mongo_items_collect.create_mongo_todo_item()
        
        return index()


    @app.route('/update_status', methods=['POST'])
    @login_required
    @check_user_role
    def update_status():
        
        response = mongo_items_collect.change_mongo_status()

        return index()
    
    return app
