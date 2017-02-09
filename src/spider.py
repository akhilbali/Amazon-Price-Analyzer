import requests
from bs4 import BeautifulSoup
from urllib import parse
from utility import *
from scraper import *

class Spider:

	base_url=''
	domain_name=''
	max_depth=0
	queue=set()
	crawled=set()
	depth={}

	products=set()
	product_list=[]

	def __init__ (self,base_url,domain_name,max_depth):
		Spider.base_url=base_url
		Spider.domain_name=domain_name
		Spider.queue.add(base_url)
		Spider.max_depth=max_depth
		Spider.depth[Spider.base_url]=0
		self.crawl_page("First Spider",Spider.base_url)

	@staticmethod
	def crawl_page(thread_name,page_url):
		if page_url not in Spider.crawled:
			# print (thread_name+ " depth=" +str(Spider.depth[page_url])+" crawling " + page_url)
			links=Spider.link_finder(page_url)
			if links:
				Spider.add_link_to_queue(links,Spider.depth[page_url]+1)
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
		

	@staticmethod
	def link_finder(page_url):
		headers=header()
		source_code=requests.get(page_url, headers=headers)
		if check_parse(page_url):
			# print (page_url)
			product=scrape(source_code,page_url)
			if product and product['ID'] not in Spider.products:
				Spider.products.add(product['ID'])
				Spider.product_list.append(product)
		plain_text=source_code.text 
		soup=BeautifulSoup(plain_text, "lxml")
		links=[]
		if Spider.depth[page_url]<Spider.max_depth:
			for link in soup.findAll('a'):
				url=parse.urljoin(Spider.base_url, link.get('href'))
				links.append(url)
		return links

	@staticmethod
	def add_link_to_queue(links,d):
		for url in links:
			if url in Spider.queue:
				if Spider.depth[url]>d:
					Spider.depth[url]=d
				continue
			if url in Spider.crawled:
				continue
			if Spider.domain_name!=get_domain_name(url):
				continue
			Spider.queue.add(url)
			Spider.depth[url]=d