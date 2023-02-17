import mysql.connector
from mysql.connector import Error

def create(cursor):
	try:
		# conn  =mysql.connector.connect(host="localhost",database="accentureDatabase",user="root",password="root",port="3306")
		# if conn:
		# 	print("Database connection established")
		# else:
		# 	print("Not connected")
		# cursor = conn.cursor()
		# sql = "create table users(userDd int not null, userName varchar(20))"
		sql=input("Enter your query")
		print("sql")
		cursor.execute(sql)
		print("Table is created")
	except(Exception,Error) as error:
		print(error)