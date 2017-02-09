import pymysql

db_user="root"
db_password="root"
def create_table(database):
	db = pymysql.connect("localhost",db_user,db_password,database)
	cursor=db.cursor()
	cursor.execute("DROP TABLE IF EXISTS ITEMS")
	cursor.execute("DROP TABLE IF EXISTS PRICES")
	sql="CREATE TABLE ITEMS (TITLE CHAR (250), PRICE FLOAT, URL TEXT, ASIN CHAR(15))"
	cursor.execute(sql)
	sql="CREATE TABLE PRICES (ASIN CHAR(15), PRICE FLOAT, PERIOD DATETIME)"
	cursor.execute(sql)
	db.close()

def add_data(product_list,database):
	db=pymysql.connect("localhost",db_user,db_password,database)
	cursor=db.cursor()
	cursor.execute("SELECT NOW()")
	data=cursor.fetchone()
	for product in product_list:
		query1="INSERT INTO ITEMS VALUES ('%s',%s,'%s','%s')" % (product['title'],product['price'],product['url'],product['ID']) 
		#print (query1)
		query2="INSERT INTO PRICES VALUES ('%s',%s,'%s')" % (product['ID'],product['price'],str(data[0]))
		#print (query2)
		try:
			cursor.execute(query1)
			cursor.execute(query2)
			db.commit()
		except:
			print ("Exception in Database")
			db.rollback() 
	db.close()

