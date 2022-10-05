import sqlite3

def conn(query):
    conn = sqlite3.connect('universitas.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

def read(query):
    conn = sqlite3.connect('universitas.db')
    c = conn.cursor()
    c.execute(query)
    records = c.fetchall()
    conn.commit()
    conn.close()
    return records





# conn = sqlite3.connect("universitas.db")
# c = conn.cursor()
# c.execute("SELECT * FROM data_mahasiswa")
# conn.commit()
# conn.close()

# CREATE TABLE data_mahasiswa (f_name text NOT NULL,l_name text NOT NULL,address text NOT NULL,city text NOT NULL,state text NOT NULL,zipcode integer DEFAULT 0)