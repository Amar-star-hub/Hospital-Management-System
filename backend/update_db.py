import sqlite3

DATABASE = "hospital.db"


conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()


# Add appointment columns

try:
    cursor.execute(
        "ALTER TABLE appointments ADD COLUMN type TEXT"
    )
except:
    pass


try:
    cursor.execute(
        "ALTER TABLE appointments ADD COLUMN status TEXT DEFAULT 'Pending'"
    )
except:
    pass



# Add billing table

cursor.execute("""
CREATE TABLE IF NOT EXISTS bills(

id INTEGER PRIMARY KEY AUTOINCREMENT,

patient_name TEXT,

doctor TEXT,

consultation_fee INTEGER,

medicine_charge INTEGER,

total_amount INTEGER,

payment_status TEXT DEFAULT 'Pending'

)
""")



conn.commit()

conn.close()


print("Database Updated Successfully")