import sqlite3

def conn(query):
    conn = sqlite3.connect('book_database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


def read(query):
    conn = sqlite3.connect('book_database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    conn.commit()
    conn.close()
    return records


# #for connect or create a database
# conn = sqlite3.connect("book_database.db")
# #create cursor for guide the database
# c = conn.cursor()

# c.execute(""" CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
# )
# """)

# #create commit for update our database
# conn.commit()

# #close connection
# conn.close()




#alternative
# conn = sqlite3.connect("book_database.db")
# c = conn.cursor()
# c.execute("INSERT INTO addresses VALUES(:f_name, l_name, :address, :city, :state, :zipcode)",
#         {
#             "f_name":f_name.get(),
#             "l_name":l_name.get(),
#             "address":address.get(),
#             "city":city.get(),
#             "state":state.get(),
#             "zipcode":zipcode.get()
#         }
# )