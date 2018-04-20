import requests
from bs4 import BeautifulSoup as bs
import time

from multiprocessing import Pool

def get_links():
	req = requests.get('https://beomi.github.io/beomi.github.io_old/')
	html = req.text
	soup = bs(html, 'html.parser')
	my_titles = soup.select('h3 > a')
	data = []

	for title in my_titles:
		data.append(title.get('href'))
	return data


def get_content(link):
	abs_link = 'https://beomi.github.io'+link
	req = requests.get(abs_link)
	html = req.text
	soup = bs(html, 'html.parser')
	print(soup.select('h1')[0].text)


if __name__ == '__main__':
	start_time = time.time()
#	for link in get_links():
#		get_content(link)
	pool = Pool(processes=4)
	pool.map(get_content, get_links())
	print("--- %s seconds ---" % (time.time() - start_time))
