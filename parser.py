import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://beomi.github.io/beomi.github.io_old/')

html = req.text

#header = req.headers
#status = req.status_code
#io_ok = req.ok

soup = BeautifulSoup(html, 'html.parser')


my_titles = soup.select('h3 > a')

data = {}

for title in my_titles:
	data[title.text] = title.get('href')
	print (title.text)
	print (title.get('href'))

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
	json.dump(data, json_file)
