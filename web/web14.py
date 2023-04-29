import requests
from bs4 import BeautifulSoup
from bs4 import Comment

URL1  = "http://web-14.challs.olicyber.it/"

r = requests.get(URL1)
soup = BeautifulSoup(r.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
print(comments)