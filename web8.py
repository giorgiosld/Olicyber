import requests

URL1  = "http://web-08.challs.olicyber.it/login"

data = {"username": "admin", "password": "admin"}

r = requests.post(URL1, data=data)

print(r.text)