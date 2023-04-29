import requests

URL1  = "http://web-09.challs.olicyber.it/login"

data = {"username": "admin", "password": "admin"}

r = requests.post(URL1, json=data)

print(r.text)