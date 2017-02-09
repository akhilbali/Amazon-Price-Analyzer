from flask import Flask, render_template, request
from flaskext.mysql import MySQL 
from utility import return_ASIN

DATABASE_NAME="AMAZON_PRICE_SCRAPER"
#DATABASE_NAME="PROJECT"

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']=DATABASE_NAME
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

@app.route('/')
def home():
	return render_template("home.html")


@app.route('/canvasjs.min.js')
def canvas():
	return render_template("canvasjs.min.js")

@app.route('/result', methods=["POST","GET"])
def result():
	if request.method=="POST":
		name=request.form['Name']
		ASIN = return_ASIN(name)
		#print (ASIN)
		if ASIN is None:
			return render_template("error.html",message="The requested url is not of a Valid Product")
		query="select * from ITEMS where ASIN = '%s'" % (ASIN)
		cursor=mysql.connect().cursor()
		cursor.execute(query)
		data = cursor.fetchone()
		if data is None:
			return render_template("error.html",message="The requested product is not in the database")
		#name=data[0]	price=data[1]	asin=data[3]
		details = {'title':data[0],'price':data[1],'id':data[3]}
		query = "select PRICE,PERIOD from PRICES where ASIN = '%s'" % (ASIN)
		cursor.execute(query)
		rows=cursor.fetchall()
		results=[]
		for row in rows:
			data=str(row[1]).split()
			data=list(map(int,data[0].split("-")))
			data={'year':data[0],'month':data[1]-1,'date':data[2],'price':row[0]}
			# print (data)
			results.append(data)
		return render_template("result.html",details = details, results=results)

if __name__=="__main__":
	app.run(debug=True)