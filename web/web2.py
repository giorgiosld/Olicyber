import requests

URL  = "http://web-02.challs.olicyber.it/server-records"

param = {"id": "flag"}
r = requests.get(URL, params=param)

print(r.text)