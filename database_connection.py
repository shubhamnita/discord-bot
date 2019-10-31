import pymysql
from credentials_store import db_host,db_port,db_name,db_user,db_password


def create_connection():
	"""
	Return mysql connection object.
	"""	
	conn = pymysql.connect(db_host, db=db_name, port=db_port,
                           user=db_user, passwd=db_password)
	return conn

def create_search_table():
	"""
	Creates search_history table which stores user search history .
	"""
	conn = create_connection()
	with conn:
		cursor = conn.cursor()
		cursor.execute("create table if not exists search_history (user VARCHAR(255),search_keyword VARCHAR(255))")
