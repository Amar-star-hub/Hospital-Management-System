import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

try:
    cursor.execute("SELECT username, password FROM admin")
    rows = cursor.fetchall()

    if rows:
        print("Admin Accounts:")
        for row in rows:
            print("Username:", row[0], "Password:", row[1])
    else:
        print("No admin account found.")

except Exception as e:
    print("Error:", e)

conn.close()