import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {
	'userId': 'my_user_id',
	'userPassword': 'my_password'
}

#with requests.Session() as s:
#	req = s.get('https://www.clien.net/service/')
#	html = req.text
#	header = req.headers
#	status = req.status_code
#	is_ok = req.ok


with requests.Session() as s:
	first_page = s.get('https://www.clien.net/service')
	html = first_page.text
	soup = bs(html, 'html.parser')
	csrf = soup.find('input', {'name': '_csrf'})

	print(csrf['value'])
	LOGIN_INFO = {**LOGIN_INFO, **{'_csrf':csrf['value']}}


	login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
	print(login_req.status_code)
