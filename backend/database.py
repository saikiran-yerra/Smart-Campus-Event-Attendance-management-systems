import mysql.connector


def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sai12345",
        database="smart_campus"
    )

    return connection