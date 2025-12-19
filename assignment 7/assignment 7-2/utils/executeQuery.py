from utils.dbconnection import getDBConnection

def executeQuery(query):
    connection=getDBConnection()

    cursor=connection.cursor()

    cursor.execute(query)

    connection.commit()

    cursor.close()

    connection.close()

