import requests, re
from bs4 import BeautifulSoup as bs

req = requests.get('https://clien.net/service/board/jirum?category=해외구매정보')
html = req.text

soup = bs(html, 'html.parser')
clien_href_list = []
clien_href_pre_string = "https://www.clien.net"

for pre in soup.findAll("div", {"class":"list_item symph_row"}):
	div_title_block = pre.div.next_sibling.next_sibling
	# print(div_title_block)
	print("------- break line -----")
	# print(div_title_block.a['href'])
	# print(div_title_block.span.next_sibling.next_sibling)
	div_title = div_title_block.span.next_sibling.next_sibling.string
	print(div_title)
	post_num, remainder = div_title_block.a['href'].split("?")
	full_target_url = clien_href_pre_string + post_num
	if (re.search('\[ebay\]', div_title, re.IGNORECASE)) or (re.search('\[e\]', div_title, re.IGNORECASE)):
		print("Ebay")
		print(full_target_url)
		clien_href_list.append(full_target_url)
	elif (re.search('\[amazon\]', div_title, re.IGNORECASE)) or (re.search('\[a\]', div_title, re.IGNORECASE)):
		print("Amazon")
		print(full_target_url)
		clien_href_list.append(full_target_url)
	else:
		print("NONE")
		print(full_target_url)
	

# for href in clien_href_list:
# 	post_id, b = href.split("?")
# 	print(post_id)
# 	print(clien_href_pre_string + post_id)