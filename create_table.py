import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect("database.db")
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the table if already exists.
# cursor_obj.execute("DROP TABLE IF EXISTS")
 
# Creating table
table = """ CREATE TABLE STUDENT (
            Name CHAR(25) NOT NULL,
            ID INT,
            Points INT,
            PRIMARY KEY(ID)
        ); """
 
cursor_obj.execute(table)
 
print("Table is Ready")
 
# Close the connection
connection_obj.close()

