from mysqlDBconnect import *

def insert(cursor,conn):
	try:
		# conn = connect()
	
		# cursor = conn.cursor()
		sql = "insert into orders(oid,orderitem,quantity) values (%s,%s,%s)"

		toid = int(input("Enter order id"))
		titem = input("Enter order item name")
		tqty = int(input("Enter order quantity"))
		
		data = [(toid,titem,tqty)]
	
		cursor.executemany(sql,data)
		conn.commit()
		print("Record inserted....")

	except(Exception,Error) as error:
		print("error")