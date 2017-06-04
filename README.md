# Amazon-Price-Analyzer

<h3>Description</h3>
<p>Amazon Price Analyzer is a web crawler application which records the prices of products at various instants of time on an e-commerce website like Amazon and helps to analyze the various trends in the price of the commodities.</p>

<h3>Application Details</h3>
<p>The application crawls the website starting from a base url upto a given depth,and scrapes the web pages for the information relating to Product Title,Product Price and Product ID.This data relating to products is stored in the database along with the timestamp.The database is then updated at regular intervals to store the new value of price along with the timestamp.User can then view the trends in the form of chart by providing the url of the product.</p> 

<h3>System Requirements</h3>
<p>The system must have a Python3 interpreter and MySQL database server.The following python modules also need to be supported by the system:</p>
1. Flask(a micro-web framework)</br>
2. flaskext.mysql
3. pymysql(sudo pip install pymysql)
4. bs4 (BeautifulSoup module)
5. urllib
6. requests

<h3>How to Run</h3>
<p>Make changes in the "main.py" script pretaining to database configuration,base url(the url from which the application starts crawling) and the depth(the maximum depth upto which the crawler crawls).</p>
<p>Execute the "main.py" script and the initial data would be stored in the database.</p>
<p>To upadte the database, execute the "update.py" script.It would add new entry of price-timestamp to the databse.</p>
<p>To view the price graph of a particular product, execute the "web.py" script and go to local-host "http://localhost:5000/" of your system.Enter the url of the desired product there and view the results.</p>
Note: Also make database configuration changes in "database.py","web.py" and "update.py"
