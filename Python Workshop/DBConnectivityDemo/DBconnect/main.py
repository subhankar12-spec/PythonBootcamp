from mysqlDBconnect import *
from createTable import create
from insertData import insert
from deleteRecord import delete
from updateRecord import update

try:
    conn = connect()
    if(conn):
        print("Database Connected")
    else:
        print("Database Not Connected")
    cursor = conn.cursor()
    while(True):
        query=input("1.Create 2.Insert 3.Display 4.Delete 5.Update")
        if(query=='Create'):
            create(cursor)
        elif query=='Insert':
            insert(cursor,conn) 
        elif query=='Delete':
            delete(conn)  
        elif query=='Update':
            update(conn)        

except(Exception,Error) as error:
	print("error")