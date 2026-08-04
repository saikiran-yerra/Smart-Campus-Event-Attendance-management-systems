async function login() {

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:5000/login", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            email: email,
            password: password
        })

    });


    const data = await response.json();


    if (response.status === 200) {

        alert(data.message);

        window.location.href = "dashboard.html";

    } else {

        alert(data.message);

    }

}


function register() {

    alert("Registration successful");

}


function createEvent() {

    alert("Event created");

}


function markAttendance() {

    alert("Attendance marked");

}