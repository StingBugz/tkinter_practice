import mysql.connector


def conn(query):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="tabelperiodik118",
        database="test"
    )
    c = conn.cursor()
    c.execute(query)
    conn.commit()

def read(query):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="tabelperiodik118",
        database="test"
    )
    c = conn.cursor()
    c.execute(query)
    data = c.fetchall()
    conn.commit()
    return data

