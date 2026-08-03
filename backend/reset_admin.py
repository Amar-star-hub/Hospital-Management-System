import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

# Delete old admin
cursor.execute("DELETE FROM admin")

# Create new admin
cursor.execute("""
INSERT INTO admin(username, password)
VALUES('admin', '1234')
""")

conn.commit()
conn.close()

print("✅ Admin account reset successfully!")
print("Username: admin")
print("Password: 1234")