import requests

URL  = "http://web-04.challs.olicyber.it/users"

header = {'Accept': 'application/xml'}
r = requests.get(URL, headers=header)

print(r.text)