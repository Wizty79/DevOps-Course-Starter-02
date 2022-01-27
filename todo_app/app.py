from flask import Flask, render_template, request
from todo_app.data.session_items import add_item, get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items = items)

@app.route('/create-todo', methods=['Post'])
def create_new_todo():
    new_todo_title = request.form['todo-name']
    add_item(new_todo_title)
    return index()
