import requests
from lxml import html
import re
from utility import *

def scrape(html_code,page_url):
	tree = html.fromstring(html_code.content)
	# tree.xpath() returns a list of HtmlElements
	product = {}
	try:
		name=tree.xpath('//*[@id="productTitle"]/text()')
		name=name[0].strip()
		product['title']=name
		#price=tree.xpath('//*[@id="priceblock_ourprice"]/text()')
		price=tree.xpath('//*[@id="price"]/table//span[starts-with(@id,"priceblock")]//text()')
		price=price[1].strip()
		price=remove_commas(price)
		product['price']=price
		product['url']=page_url
		product['ID']=return_ASIN(page_url) 
		'''for i in range(1,5):
			path='//*[@id="feature-bullets"]/ul/li['+str(i)+']/span'
			description=tree.xpath(path)
			s=description[0].text
			s=s.encode('ascii','ignore')
			s=s.strip()
			s=s.decode('utf-8')
			#print (s)'''
		return product
	except:
		print ("Error Occured")
		product={}
		return product 


def check_parse(url):
	allowed_pattern=re.compile(r'(/)([A-Z])([A-Z0-9]){9}(/)')
	result=allowed_pattern.search(url)
	denied_pattern=[r'/product-reviews/', r'/offer-listing/'] 
	if result is None:
		return False
	else:
		# print (result.group())
		for s in denied_pattern:
			d=re.compile(s)
			deny= d.search(url)
			if deny is not None:
				return False
		return True
