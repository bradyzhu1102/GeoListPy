from mysql.connector import errorcode


def getByID(cnx, id):
	cursor = cnx.cursor()
	query = ("SELECT Latitude, Longitude FROM GEONAMES WHERE Id = {}".format(id))
	cursor.execute(query)
	result = cursor.fetchall()
	cursor.close()
	return result

def getByName(cnx, name):
	cursor = cnx.cursor()
	query = ("SELECT Latitude, Longitude FROM GEONAMES WHERE Name = '{}'".format(name))
	cursor.execute(query)
	result = cursor.fetchall()
	cursor.close()
	return result






