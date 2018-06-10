import requests, re, time
from bs4 import BeautifulSoup as bs

req = requests.get('https://clien.net/service/board/jirum?category=해외구매정보')
html = req.text

soup = bs(html, 'html.parser')
clien_href_list = []
target_href_list = []
clien_href_pre_string = "https://www.clien.net"

for pre in soup.findAll("div", {"class":"list_item symph_row jirum"}):
	# print(pre)
	div_title_block = pre.div.next_sibling.next_sibling
	# print(div_title_block)
	# print("------- break line -----")
	# print(div_title_block.a['href'])
	# print(div_title_block.span)
	div_title = div_title_block.span.string
	# print(div_title)
	post_num, remainder = div_title_block.a['href'].split("?")
	full_target_url = clien_href_pre_string + post_num
	# print(full_target_url)
	clien_href_list.append(full_target_url)


for each_href in clien_href_list:
	item_req = requests.get(each_href)
	item_html = item_req.text
	item_soup = bs(item_html, 'html.parser')

	item_div = item_soup.find("div", {"class":"attached_link top"})
	print("------- break line -----")
	try:
		target_href_list.append(item_div.div.a['href'])
		print (item_div.div.a['href'])
	except:
		target_href_list.append("error")
	time.sleep(1)

print("------- break line -----")
print(len(clien_href_list))
print(clien_href_list)
print("------- break line -----")
print(len(target_href_list))
print(target_href_list)



	# ## distinguish source url
	# if (re.search('\[ebay\]', div_title, re.IGNORECASE)) or (re.search('\[e\]', div_title, re.IGNORECASE)):
	# 	print("Ebay")
	# 	print(full_target_url)
	# 	clien_href_list.append(full_target_url)
	# elif (re.search('\[amazon\]', div_title, re.IGNORECASE)) or (re.search('\[a\]', div_title, re.IGNORECASE)):
	# 	print("Amazon")
	# 	print(full_target_url)
	# 	clien_href_list.append(full_target_url)
	# else:
	# 	print("NONE")
	# 	print(full_target_url)
	

# for href in clien_href_list:
# 	post_id, b = href.split("?")
# 	print(post_id)
# 	print(clien_href_pre_string + post_id)
