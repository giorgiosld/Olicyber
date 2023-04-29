import requests
from bs4 import BeautifulSoup

URL1  = "http://web-12.challs.olicyber.it/"

r = requests.get(URL1)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find_all("pre"))
