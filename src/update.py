import pymysql
from utility import *
import requests
from lxml import html

db_user="root"
db_password="root"

def get_new_price(url):
	headers = header()
	html_code=requests.get(url, headers=headers)
	tree = html.fromstring(html_code.content)
	price=tree.xpath('//*[@id="price"]/table//span[starts-with(@id,"priceblock")]//text()')
	price=price[1].strip()
	price=remove_commas(price)
	return price

def update(database):
	db = pymysql.connect("localhost","root","root",database)
	cursor=db.cursor()
	cursor.execute("SELECT NOW()")
	data=cursor.fetchone()
	cursor.execute("SELECT * FROM ITEMS")
	result=cursor.fetchall()
	try:
		for row in result:
			url=row[2]
			asin=row[3]
			price = get_new_price(url)
			print (price)
			query1="UPDATE ITEMS SET PRICE= %s WHERE ASIN = '%s'" % (price,asin)
			query2="INSERT INTO PRICES VALUES ('%s',%s,'%s')" % (asin,price,str(data[0]))
			cursor.execute(query1)
			cursor.execute(query2)
		db.commit()
	except:
		traceback.print_stack()
		print ("Exception in database")
		db.rollback()


DATABASE_NAME="AMAZON_PRICE_SCRAPER"
update(DATABASE_NAME)