import requests, re, time
from bs4 import BeautifulSoup as bs

url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu4'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}
req = requests.get(url, headers=headers)
print(req.encoding)
html = req.text
print(html)

soup = bs(html, 'html.parser')
ppomppu_href_list = []
target_href_list = []
# print(soup)

# for pre in soup.findAll("td", {"valign":"middle"}):
# 	print(pre)