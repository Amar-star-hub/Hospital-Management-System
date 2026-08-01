import sqlite3


conn = sqlite3.connect("hospital.db")

cursor = conn.cursor()


cursor.execute("""
ALTER TABLE appointments
ADD COLUMN status TEXT DEFAULT 'Pending'
""")


conn.commit()

conn.close()


print("Status column added successfully!")