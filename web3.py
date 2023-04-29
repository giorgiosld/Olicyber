import requests

URL  = "http://web-03.challs.olicyber.it/flag"

header = {'X-Password': 'admin'}
r = requests.get(URL, headers=header)

print(r.text)