import requests
from bs4 import BeautifulSoup as bs

req = requests.get('https://clien.net/service/board/jirum?category=해외구매정보')
html = req.text

soup = bs(html, 'html.parser')

for d in soup.findAll("a", {"class":"list_subject"}):
    print (d)
    print (d.get('href'))
    print (d.span)
