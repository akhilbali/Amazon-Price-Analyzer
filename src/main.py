from spider import Spider
from utility import *
import threading
from queue import Queue
from scraper import *
from database import *

#defines the start url for the crawler
BASE_URL="http://www.amazon.in/Laptops/b/ref=sd_allcat_computers_laptop?ie=UTF8&node=1375424031"
domain_name=get_domain_name(BASE_URL)
#defines the maximum number of threads to be created
NUM_OF_THREADS=6
#defines the maximum depth i.e. the depth of the pages in crawling
MAX_DEPTH=1
#the name of the database
#also change this value in update.py and web.py if the name of the database is changed
DATABASE_NAME="AMAZON_PRICE_SCRAPER"


q=Queue()
Spider(BASE_URL,domain_name,MAX_DEPTH)

def create_threads():
	for _ in range(NUM_OF_THREADS):
		t=threading.Thread(target=work)
		t.daemon=True
		t.start()

def work():
	while True:
		url=q.get()
		if url is None:
			break
		Spider.crawl_page(threading.current_thread().name,url)
		q.task_done()

def crawl():
	#print (len(Spider.queue))
	links=Spider.queue.copy()
	if len(links)>0:
		for link in links:
			q.put(link)
		q.join()
		crawl()

create_threads()
crawl()

print (len(Spider.product_list))
create_table(DATABASE_NAME)
add_data(Spider.product_list,DATABASE_NAME)