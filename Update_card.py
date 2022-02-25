import requests

url = "https://api.trello.com/1/cards/620fb34b5249af284c99edc7"

querystring = {"key":"2a6a1ec21325310e0ed98efa302b2dd3","token":"e894632f11414a6d27f6df41e35edacce76d1a94287ef709cdfc73994f7d4b48","idList":"6205664a19d7b437223061ee"}

response = requests.request("PUT", url, params=querystring)

print(response.text)

