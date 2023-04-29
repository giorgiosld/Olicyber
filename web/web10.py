import requests

URL1  = "http://web-10.challs.olicyber.it/"

r = requests.options(URL1)

print(r.headers)
#valid head, options and get
r = requests.head(URL1)
print(r.headers)

r = requests.get(URL1)
print(r.text)

r = requests.put(URL1)
print(r.text)

r = requests.patch(URL1)
print(r.headers)