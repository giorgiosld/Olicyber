import requests

URL = "http://headache.challs.olicyber.it"

r = requests.options(URL)
print(r.headers)