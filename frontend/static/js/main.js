// ==========================================
// MAIN JAVASCRIPT
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("PharmaComm AI Loaded ✅");

    const logoutBtn = document.getElementById("logoutBtn");

    if (logoutBtn) {

        logoutBtn.addEventListener("click", function (e) {

            const confirmLogout = confirm("Are you sure you want to logout?");

            if (!confirmLogout) {

                e.preventDefault();

            }

        });

    }

});