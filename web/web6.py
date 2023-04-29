import requests

URL1  = "http://web-06.challs.olicyber.it/token"
URL2  = "http://web-06.challs.olicyber.it/flag"

s = requests.Session()

r = s.get(URL1)

r2 = s.get(URL2)
print(r2.text)