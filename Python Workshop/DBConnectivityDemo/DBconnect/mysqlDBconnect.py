import mysql.connector
from mysql.connector import Error
import importlib.util
# env = importlib.util.spec_from_file_location("configuration", r"C:\Users\Administrator\Desktop\DBConnectivityDemo\config\configuration.env") 
from envParser import *

def connect():
	try:
		# read the env file and get the configurations
		# print("Hello")
		params = read_db_params()
		conn = mysql.connector.connect(
				 host = params.get('DB','host'),
				 database = params.get('DB','database'),
				 user = params.get('DB','username'),
				 password = params.get('DB','password'),
				 port = params.get('DB','port')
		)
		# print("Database Connected")
		return conn
	except(Exception, Error) as error:
		print(error)