from urllib.parse import urlparse
import re

def header():
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
	return headers
	
def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''

def get_domain_name(url):
	try:
		domain=get_sub_domain_name(url).split(".")
		return domain[-2]+"."+domain[-1]
	except:
		return ''

#this functions removes "," from the price string so that it could be saved as int or float
def remove_commas(price):
	str_price=price.split(",")
	price=""
	for p in str_price:
		price = price+p
	return price

#this fuction returns the Amazon product unique ASIN from the given url/string 
def return_ASIN(string):
	allowed_pattern=re.compile(r'(/)([A-Z])([A-Z0-9]){9}(/)')
	result=allowed_pattern.search(string)
	if result is None:
		return None
	ASIN = (str(result.group(0)))[1:11]
	return ASIN 