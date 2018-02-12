import mysql.connector as connector
from mysql.connector import errorcode
import sys

from config import config
import getCoord

# please make sure you have installed mysql-connector-python-rf
# after installing mysql, 
# use '''pip3 install mysql-connector-python-rf'''

# used as mass geocoordinate extractor
if __name__ == "__main__":

	# connect to local mysql database
	try: 
		cnx = connector.connect(**config)

	except connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Eccess denied, please check your host, user and password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Unknown Database, please check database name")
		else:
			print(err)

	print("Note: Input 'exit' to terminate")
	while True:

		method = input("Choose one method from [getByID, getByName, exit]: ")

		if method == "getByID":
			Id = input("ID: ")
			coord = getCoord.getByID(cnx, Id)
			print(coord[0][0], coord[0][1])

		elif method == "getByName":
			Name = input("Name: ")
			coord = getCoord.getByName(cnx, Name)
			for co in coord:
				print(co[0], co[1])

		elif method == "exit":
			sys.exit()

		else:
			print("Unknown method")






	
