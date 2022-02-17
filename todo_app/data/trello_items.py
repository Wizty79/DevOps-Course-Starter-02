import requests 
import dotenv 
import os

url = "https://api.trello.com/1/members/me/boards"

env_file = dotenv.load_dotenv(".env")

querystring = {"key":"API_KEY", "token":"API_TOKEN"}

response - requests.request("GET", yrl, params=querystring)

print(response.text)


