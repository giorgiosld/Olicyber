import requests
from bs4 import BeautifulSoup

URL1  = "http://web-13.challs.olicyber.it/"

r = requests.get(URL1)
soup = BeautifulSoup(r.text, 'html.parser')
spans = soup.find_all('span')
flag = ""
for span in spans:
    flag += str(span)[18:-7]
    
print("flag{"+flag+"}")