import configparser

def read_db_params():
	# read the properties from env file

	config = configparser.ConfigParser()
	config.read('configuration.env')
	return config