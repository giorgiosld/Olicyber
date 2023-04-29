import requests

URL1  = "http://web-07.challs.olicyber.it/"

r = requests.head(URL1)

print(r.headers)