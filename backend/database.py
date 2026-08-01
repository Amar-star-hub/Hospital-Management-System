import sqlite3


DATABASE = "hospital.db"


conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()



# =========================
# ADMIN TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS admin(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT NOT NULL UNIQUE,

    password TEXT NOT NULL

)
""")


# Default Admin Account

cursor.execute("""
INSERT INTO admin(username,password)

SELECT 'admin','1234'

WHERE NOT EXISTS
(
SELECT * FROM admin
WHERE username='admin'
)
""")





# =========================
# PATIENT TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    age INTEGER,

    gender TEXT,

    phone TEXT,

    disease TEXT

)
""")







# =========================
# APPOINTMENT TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_name TEXT NOT NULL,

    doctor TEXT NOT NULL,

    appointment_date TEXT NOT NULL,

    phone TEXT,

    disease TEXT,

    type TEXT DEFAULT 'Regular Checkup',

    status TEXT DEFAULT 'Pending'

)
""")







# =========================
# DOCTOR TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    specialization TEXT,

    phone TEXT

)
""")





# Default Doctors

cursor.execute("""
INSERT INTO doctors(name,specialization,phone)

SELECT 
'Dr. Patil',
'Cardiologist',
'9876543210'

WHERE NOT EXISTS
(
SELECT * FROM doctors
WHERE name='Dr. Patil'
)
""")


cursor.execute("""
INSERT INTO doctors(name,specialization,phone)

SELECT 
'Dr. Sharma',
'Neurologist',
'9876543211'

WHERE NOT EXISTS
(
SELECT * FROM doctors
WHERE name='Dr. Sharma'
)
""")


cursor.execute("""
INSERT INTO doctors(name,specialization,phone)

SELECT 
'Dr. Kulkarni',
'General Physician',
'9876543212'

WHERE NOT EXISTS
(
SELECT * FROM doctors
WHERE name='Dr. Kulkarni'
)
""")


cursor.execute("""
INSERT INTO doctors(name,specialization,phone)

SELECT 
'Dr. Deshmukh',
'Orthopedic',
'9876543213'

WHERE NOT EXISTS
(
SELECT * FROM doctors
WHERE name='Dr. Deshmukh'
)
""")








# =========================
# BILL TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS bills(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_name TEXT,

    doctor TEXT,

    consultation_fee INTEGER,

    medicine_charge INTEGER,

    total_amount INTEGER,

    payment_status TEXT DEFAULT 'Pending',

    bill_date TEXT

)
""")








# =========================
# SAVE DATABASE
# =========================

conn.commit()

conn.close()



print("Hospital Database Created Successfully!")