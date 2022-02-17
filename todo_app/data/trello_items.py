import requests 
import dotenv 
import os

url = "https://api.trello.com/1/boards/6205664a19d7b437223061eb/lists"

dotenv.load_dotenv(".env")

print(os.getenv("API_KEY"))

querystring = {"key":os.getenv("API_KEY"),"token":os.getenv("API_TOKEN"),"cards": "open"}

response - requests.request("GET", url, params=querystring)

print(response.text)

