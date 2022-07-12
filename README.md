# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Create a safe storage for your app to-do items 

 * Create a Trello account 

 * Create a Trello board on your account to be used by the app for storing the to-do items from the app

 * Create a To-Do and Done list on the board

 * Get your Trello API key and generate a API Token as well. 

 * Get the To-Do and Do list ID's,as well as the board id, one way of doing this would be to use a service like Postman or Hoppscotch to make API requests.  

  * Add the Trello API key, token, board and list ID's as variables in the .env file. they should be named as followes: API_KEY, API_TOKEN, TRELLO_BOARD_ID, TRELLO_TODO_LIST_ID, and TRELLO_DONE_LIST_ID. 
  Note if using a virtual machine like Gitpod exclusively, you will have to re-add these variables to the .env file at the start of every new session as you will have no local copy of the code and the file will not be committed to the repo due to security reasons. (the .env files it added to the .gitignore file).

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Testing the App

If you are experiencing issues with the App after making your own changes, you'll find two unit tests are ready to run to test that the View_model class is sorting the items as intended. You'll also find an integration test intended to test the app.py code base itself and the Trello API calls it makes. 

If not already install, you'll need pytest, you can do this by running the command(please not if your using a virtual machine you may need to install this every time you start a new session):
```bash
$ pip install pytest 
```
you can run the tests by running the command:
```bash
$ poetry run pytest 
```

## launching the To-Do App onto a virtual Machine using Ansible 

You can provision a VM from an Ansible Control Node by running the command "ssh user_name@IP_of_Ansible_controller", you will then be asked "Are you sure you want to continue connecting (yes/no/[fingerprint])? " just say yes and provide the password when prompted.  

You can now continue setting up your ansible playbook if you haven't already (see example in this code base or the official Ansible documentation https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#about-playbooks). 
 
## launching the todo-app into a container (Docker in this case)

Tip: if you have white/blank space in your code base or after a line of code, make sure to delete it; while Python may be able to understand the code just fine, Docker is much more sensitive and will through errors even with one single blankspace after a line of code (lesson hard learned). 

First you'll need to install Docker, please see this link https://www.docker.com/products/docker-desktop/ (if unsing Gitpod you can simply do this by using pip install).
For help regarding writing a Docker file, please see the documentation https://docs.docker.com/desktop/

See below for the commands to run the Dockerfile in various modes/versions (see the code base for examples as to how multi-stage build have been used to have a production and developer mode/version) 
See this link for more info regarding multi-stage builds https://docs.docker.com/develop/develop-images/multistage-build/

Run and overriding the entrypoint to use bash:
docker run --env-file ./.env -p 5000:5000 --entrypoint bash -it todo-app

Build the image:
docker build --tag todo-app .

Run the image:
docker run --env-file ./.env -p 5000:5000 todo-app

Build the production version:
docker build --tag todo-app:prod --target prodpy .

Run the production version:
docker run --env-file ./.env -p 5000:5000 todo-app:prod

Build the developer version:
docker build --tag todo-app:dev --target devpy .

Run the developer version:
docker run --env-file ./.env -p 5000:5000 todo-app:dev

Bind Mount and volume in dev version:
Generally you can bind mount by using the option --mount
See the following command to use for this specific codebase:

docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev

Run all tests inside Docker:

Build the Container:
docker build --tag todo-app:devtest --target devtestpy .

Run the tests in Docker:
docker run --env-file ./.env -p 5000:5000 todo-app:devtest

For more details see the following link regarding the use of bind mounts:
https://docs.docker.com/storage/bind-mounts/?msclkid=91003082cf8011ec99b6a62f98d6305a

And see this link regarding the use of volumes:
https://docs.docker.com/storage/volumes/

Please note that in this code base the .env file have been added to a .dockerignore file for security reasons. 
See this link for more info regarding the use of the dockerignore file: 
https://docs.docker.com/engine/reference/builder/#dockerignore-file


