import mysql.connector

def conn(query):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="test"
    )
    c = conn.cursor()
    c.execute(query)
    conn.commit()
