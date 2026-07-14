// ==========================================
// DASHBOARD JAVASCRIPT
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    // Greeting
    const greeting = document.getElementById("greeting");

    if (greeting) {

        const hour = new Date().getHours();

        if (hour < 12) {

            greeting.innerHTML = "Good Morning, Turvi!";

        }

        else if (hour < 17) {

            greeting.innerHTML = "Good Afternoon, Turvi!";

        }

        else {

            greeting.innerHTML = "Good Evening, Turvi!";

        }

    }

});