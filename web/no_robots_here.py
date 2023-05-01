import requests
from bs4 import BeautifulSoup

URL = "http://no-robots.challs.olicyber.it/"

r = requests.get(URL)
print(r.text)

ROBOTS = URL+"robots.txt"
r = requests.get(ROBOTS)
print(str(r.text)[24:])
FLAG_URI = str(r.text)[24:]

FLAG = URL+FLAG_URI
r = requests.get(FLAG)
soup = BeautifulSoup(r.text, 'html.parser')
flag = soup.find_all('h2')
print(str(flag)[5:-5])