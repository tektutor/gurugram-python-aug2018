import mysql.connector

mydb = mysql.connector.connect ( host="localhost", user='user', passwd='passwd', database='test )

mycursor = mydb.cursor()

mycursor.execute ( "CREATE TABLE customers(name VARCHAR(25), address VARCHAR(255) )" )

