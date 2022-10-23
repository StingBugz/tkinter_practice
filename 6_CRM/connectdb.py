import mysql.connector

def conn(query):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="crm"
    )
    c = conn.cursor()
    c.execute(query)
    conn.commit()

def read(query):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="crm"
    )
    c = conn.cursor()
    c.execute(query)
    alldata = c.fetchall()
    conn.commit()
    return alldata