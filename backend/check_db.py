import sqlite3
import os

DATABASE = os.path.join(os.path.dirname(__file__), "hospital.db")

print("Database path:", DATABASE)

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cursor.fetchall())

conn.close()

print("Done")