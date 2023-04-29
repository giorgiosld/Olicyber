import requests 

URL = "http://web-01.challs.olicyber.it/"

r = requests.get(URL)

print(r.text)