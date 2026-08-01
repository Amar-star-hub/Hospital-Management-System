from flask import Flask, render_template, request, redirect, session
import sqlite3
import os


app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)


app.secret_key = "hospital_secret_key"


DATABASE = os.path.join(
    os.path.dirname(__file__),
    "hospital.db"
)



# ================= DATABASE =================

def connect():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn





# ================= LOGIN CHECK =================

def login_required():

    if "admin" not in session:
        return False

    return True





# ================= HOME =================

@app.route("/")
def home():

    return render_template("index.html")






# ================= LOGIN =================

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method=="POST":


        username=request.form["username"]

        password=request.form["password"]


        conn=connect()


        user=conn.execute(
        """
        SELECT * FROM admin
        WHERE username=? AND password=?
        """,
        (username,password)

        ).fetchone()



        conn.close()



        if user:

            session["admin"]=username

            return redirect("/dashboard")


        else:

            return "Invalid Username or Password"



    return render_template("login.html")







# ================= LOGOUT =================


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")







# ================= DOCTOR =================


@app.route("/doctors")
def doctors():

    return render_template("doctor.html")







# ================= PATIENT MODULE =================



@app.route("/patients")
def patients():

    return render_template("patient.html")







@app.route("/register_patient",methods=["POST"])
def register_patient():


    conn=connect()


    conn.execute(
    """
    INSERT INTO patients

    (name,age,gender,phone,disease)

    VALUES(?,?,?,?,?)

    """,

    (
    request.form["name"],
    request.form["age"],
    request.form["gender"],
    request.form["phone"],
    request.form["disease"]
    )

    )


    conn.commit()

    conn.close()


    return redirect("/patient_list")








@app.route("/patient_list")
def patient_list():


    if not login_required():

        return redirect("/login")



    conn=connect()


    patients=conn.execute(
        "SELECT * FROM patients"
    ).fetchall()



    conn.close()



    return render_template(
        "patient_list.html",
        patients=patients
    )







@app.route("/edit_patient/<int:id>")
def edit_patient(id):


    if not login_required():

        return redirect("/login")



    conn=connect()



    patient=conn.execute(
    """
    SELECT * FROM patients
    WHERE id=?
    """,
    (id,)
    ).fetchone()



    conn.close()



    return render_template(
        "edit_patient.html",
        patient=patient
    )








@app.route("/update_patient/<int:id>",methods=["POST"])
def update_patient(id):


    if not login_required():

        return redirect("/login")



    conn=connect()



    conn.execute(
    """
    UPDATE patients

    SET

    name=?,
    age=?,
    gender=?,
    phone=?,
    disease=?

    WHERE id=?

    """,

    (

    request.form["name"],
    request.form["age"],
    request.form["gender"],
    request.form["phone"],
    request.form["disease"],
    id

    )

    )



    conn.commit()

    conn.close()



    return redirect("/patient_list")







@app.route("/delete_patient/<int:id>")
def delete_patient(id):


    if not login_required():

        return redirect("/login")



    conn=connect()



    conn.execute(
    "DELETE FROM patients WHERE id=?",
    (id,)
    )



    conn.commit()

    conn.close()



    return redirect("/patient_list")
# ================= APPOINTMENT MODULE =================


@app.route("/appointments")
def appointments():

    return render_template("appointment.html")






# ================= BOOK APPOINTMENT =================


@app.route("/book_appointment",methods=["POST"])
def book_appointment():


    if not login_required():

        return redirect("/login")



    conn=connect()



    conn.execute(
    """
    INSERT INTO appointments

    (
    patient_name,
    doctor,
    appointment_date,
    phone,
    disease,
    type
    )

    VALUES(?,?,?,?,?,?)

    """,

    (

    request.form["patient_name"],

    request.form["doctor"],

    request.form["appointment_date"],

    request.form["phone"],

    request.form["disease"],

    request.form["type"]

    )

    )



    conn.commit()

    conn.close()



    return redirect("/appointment_list")








# ================= APPOINTMENT LIST =================


@app.route("/appointment_list")
def appointment_list():


    if not login_required():

        return redirect("/login")



    conn=connect()



    appointments=conn.execute(

        "SELECT * FROM appointments"

    ).fetchall()



    conn.close()



    return render_template(

        "appointment_list.html",

        appointments=appointments

    )







# ================= EDIT APPOINTMENT =================


@app.route("/edit_appointment/<int:id>")
def edit_appointment(id):


    if not login_required():

        return redirect("/login")



    conn=connect()



    appointment=conn.execute(

    """
    SELECT * FROM appointments
    WHERE id=?

    """,

    (id,)

    ).fetchone()



    conn.close()



    return render_template(

        "edit_appointment.html",

        appointment=appointment

    )








# ================= UPDATE APPOINTMENT =================


@app.route("/update_appointment/<int:id>",methods=["POST"])
def update_appointment(id):


    if not login_required():

        return redirect("/login")



    conn=connect()



    conn.execute(

    """

    UPDATE appointments

    SET

    patient_name=?,

    doctor=?,

    appointment_date=?,

    phone=?,

    disease=?,

    type=?



    WHERE id=?

    """,


    (

    request.form["patient_name"],

    request.form["doctor"],

    request.form["appointment_date"],

    request.form["phone"],

    request.form["disease"],

    request.form["type"],

    id

    )


    )



    conn.commit()

    conn.close()



    return redirect("/appointment_list")









# ================= DELETE APPOINTMENT =================


@app.route("/delete_appointment/<int:id>")
def delete_appointment(id):


    if not login_required():

        return redirect("/login")



    conn=connect()



    conn.execute(

    "DELETE FROM appointments WHERE id=?",

    (id,)

    )



    conn.commit()

    conn.close()



    return redirect("/appointment_list")









# ================= UPDATE APPOINTMENT STATUS =================


@app.route("/update_status/<int:id>/<status>")
def update_status(id,status):


    if not login_required():

        return redirect("/login")



    conn=connect()



    conn.execute(

    """

    UPDATE appointments

    SET status=?

    WHERE id=?

    """,

    (

    status,

    id

    )

    )



    conn.commit()

    conn.close()



    return redirect("/appointment_list")
# ================= BILLING MODULE =================


@app.route("/billing")
def billing():


    if not login_required():

        return redirect("/login")



    return render_template("billing.html")








# ================= CREATE BILL =================


@app.route("/create_bill",methods=["POST"])
def create_bill():


    if not login_required():

        return redirect("/login")



    patient_name=request.form["patient_name"]

    doctor=request.form["doctor"]

    consultation_fee=int(request.form["consultation_fee"])

    medicine_charge=int(request.form["medicine_charge"])



    total_amount = consultation_fee + medicine_charge



    conn=connect()



    conn.execute(

    """

    INSERT INTO bills

    (

    patient_name,

    doctor,

    consultation_fee,

    medicine_charge,

    total_amount

    )


    VALUES(?,?,?,?,?)

    """,


    (

    patient_name,

    doctor,

    consultation_fee,

    medicine_charge,

    total_amount

    )

    )



    conn.commit()

    conn.close()



    return redirect("/bill_list")









# ================= BILL LIST =================


@app.route("/bill_list")
def bill_list():


    if not login_required():

        return redirect("/login")



    conn=connect()



    bills=conn.execute(

    "SELECT * FROM bills"

    ).fetchall()



    conn.close()



    return render_template(

        "bill_list.html",

        bills=bills

    )









# ================= DELETE BILL =================


@app.route("/delete_bill/<int:id>")
def delete_bill(id):


    if not login_required():

        return redirect("/login")



    conn=connect()



    conn.execute(

    "DELETE FROM bills WHERE id=?",

    (id,)

    )



    conn.commit()

    conn.close()



    return redirect("/bill_list")









# ================= UPDATE PAYMENT =================


@app.route("/update_payment/<int:id>/<status>")
def update_payment(id,status):


    if not login_required():

        return redirect("/login")



    conn=connect()



    conn.execute(

    """

    UPDATE bills

    SET payment_status=?

    WHERE id=?

    """,

    (

    status,

    id

    )

    )



    conn.commit()

    conn.close()



    return redirect("/bill_list")










# ================= DASHBOARD =================


@app.route("/dashboard")
def dashboard():


    if not login_required():

        return redirect("/login")



    conn=connect()



    total_patients=conn.execute(

    "SELECT COUNT(*) FROM patients"

    ).fetchone()[0]




    total_appointments=conn.execute(

    "SELECT COUNT(*) FROM appointments"

    ).fetchone()[0]




    pending=conn.execute(

    """

    SELECT COUNT(*)

    FROM appointments

    WHERE status='Pending'

    """

    ).fetchone()[0]




    confirmed=conn.execute(

    """

    SELECT COUNT(*)

    FROM appointments

    WHERE status='Confirmed'

    """

    ).fetchone()[0]




    completed=conn.execute(

    """

    SELECT COUNT(*)

    FROM appointments

    WHERE status='Completed'

    """

    ).fetchone()[0]





    total_bills=conn.execute(

    "SELECT COUNT(*) FROM bills"

    ).fetchone()[0]





    conn.close()





    return render_template(

        "dashboard.html",

        total_patients=total_patients,

        total_appointments=total_appointments,

        pending=pending,

        confirmed=confirmed,

        completed=completed,

        total_bills=total_bills

    )









# ================= CONTACT =================


@app.route("/contact")
def contact():

    return render_template("contact.html")









# ================= RUN SERVER =================


if __name__=="__main__":


    app.run(debug=True)