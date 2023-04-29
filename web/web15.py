import requests
from bs4 import BeautifulSoup

URL1  = "http://web-15.challs.olicyber.it/"

r = requests.get(URL1)
print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('link')
scripts = soup.find_all('script')
print(links)
print(scripts)
