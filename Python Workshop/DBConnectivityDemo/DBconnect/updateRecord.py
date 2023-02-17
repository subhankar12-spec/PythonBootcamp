from mysqlDBconnect import *


def get_by_id(cursor,oeid):
    sql = "select * from orders where orderitem = %s;"
    cursor.execute(sql,[oeid])
    return cursor.fetchone()


def update(conn):
    cursor = conn.cursor()
    oeid = input("Enter the old order Item")
    neid = input("Enter the current order item name")
    query = "update orders set orderitem= %s where orderitem= %s;"
    print(query)
    try:
        record = get_by_id(cursor,oeid)
        if record is None:
            print("Order is not found for given id")
        else:
            cursor.execute(query, [neid,oeid])
            conn.commit()
            print("OrderItem is = {} updated to".format(neid))
    except(Exception,Error) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         cursor.close()
    #         conn.close()
    #         print("connections are closed")
