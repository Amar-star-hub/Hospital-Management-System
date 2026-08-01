// Load appointments from Local Storage
let appointments = JSON.parse(localStorage.getItem("appointments")) || [];

// Run only if appointment table exists
window.onload = function () {
    if (document.getElementById("appointmentTable")) {
        displayAppointments();
    }
};

// Book Appointment
function bookAppointment() {

    let name = document.getElementById("name").value;
    let doctor = document.getElementById("doctor").value;
    let date = document.getElementById("date").value;
    let phone = document.getElementById("phone").value;

    if (name === "" || doctor === "" || date === "" || phone === "") {
        alert("Please fill all fields.");
        return false;
    }

    let appointment = {
        name: name,
        doctor: doctor,
        date: date,
        phone: phone
    };

    appointments.push(appointment);

    localStorage.setItem("appointments", JSON.stringify(appointments));

    displayAppointments();

    document.querySelector("form").reset();

    alert("Appointment Booked Successfully!");

    return false;
}

// Display Appointments
function displayAppointments() {

    let table = document.getElementById("appointmentTable");

    // Stop if table doesn't exist
    if (!table) {
        return;
    }

    table.innerHTML = `
        <tr>
            <th>Patient</th>
            <th>Doctor</th>
            <th>Date</th>
            <th>Phone</th>
            <th>Action</th>
        </tr>
    `;

    appointments.forEach((appointment, index) => {

        let row = table.insertRow();

        row.insertCell(0).innerHTML = appointment.name;
        row.insertCell(1).innerHTML = appointment.doctor;
        row.insertCell(2).innerHTML = appointment.date;
        row.insertCell(3).innerHTML = appointment.phone;

        row.insertCell(4).innerHTML =
            `<button onclick="deleteAppointment(${index})">Delete</button>`;
    });
}

// Delete Appointment
function deleteAppointment(index) {

    appointments.splice(index, 1);

    localStorage.setItem("appointments", JSON.stringify(appointments));

    displayAppointments();
}

// Search Appointment
function searchAppointment() {

    let input = document.getElementById("searchInput");

    // Stop if search box doesn't exist
    if (!input) {
        return;
    }

    let filter = input.value.toUpperCase();

    let table = document.getElementById("appointmentTable");

    if (!table) {
        return;
    }

    let tr = table.getElementsByTagName("tr");

    for (let i = 1; i < tr.length; i++) {

        let td = tr[i].getElementsByTagName("td")[0];

        if (td) {

            let txtValue = td.textContent || td.innerText;

            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}