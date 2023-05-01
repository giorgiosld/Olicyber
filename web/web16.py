from requests import Response, get
from bs4 import BeautifulSoup, ResultSet

URL1  = "http://web-16.challs.olicyber.it"

def clean_links(links: set) -> set:
    links_to_retrieve = set()
    for link in links:
        links_to_retrieve.add(str(link)[9:24])
    return links_to_retrieve

def search_in_link(text: Response) -> ResultSet:
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')
    flag = soup.find_all('h1')
    print(flag)
    return links

def visit_links(links_to_visit: set):
    new_links_to_visit = set()
    new_links_to_visit.update(links_to_visit)
    for link in links_to_visit:
        r = get(URL1+link)
        soup = BeautifulSoup(r.text, 'html.parser')
        links = soup.find_all('a')
        flag = soup.find_all('h1')
        print(flag)
        if(str(flag)[:10] == "[<h1>flag{"):
            print(f"Flag found!!! {str(flag)[5:26]}")
            exit(0)
        new_links_to_visit.update(clean_links(links))
    visit_links(new_links_to_visit)

r = get(URL1)
links = search_in_link(r)
links_to_visit = clean_links(links)
visit_links(links_to_visit)
