import sqlite3
import os

#connection 

conn = sqlite3.connect("../data/olist.sqlite")
cursor = conn.cursor()

#get all table names 
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables",[t[0] for t in tables])

#loop through tables and printing its names 
for table in tables:
    print(f"\nTables: {table[0]}")
    cursor.execute(f"PRAGMA table_info({table[0]});")
    columns = cursor.fetchall()
    for col in columns:
        print(f" -{col[1]} ({col[2]})")