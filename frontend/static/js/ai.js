console.log("AI JS Loaded");

document.addEventListener("DOMContentLoaded", function () {

    const button = document.getElementById("generateBtn");
    const loading = document.getElementById("loadingSection");
    const result = document.getElementById("resultSection");

    if (!button) return;

    button.addEventListener("click", function () {

        button.disabled = true;

        button.innerHTML =
            '<span class="spinner-border spinner-border-sm me-2"></span>Generating...';

        loading.style.display = "block";

        result.style.display = "none";

        setTimeout(function () {

            loading.style.display = "none";

            result.style.display = "block";

            button.disabled = false;

            button.innerHTML =
                '<i class="bi bi-stars me-2"></i>Generate';

        }, 2000);

    });

});
// ===========================
// Audience Selection
// ===========================

document.addEventListener("DOMContentLoaded", function () {

    const audienceMethod = document.getElementById("audienceMethod");
    const smartFilters = document.getElementById("smartFiltersSection");
    const manualSelection = document.getElementById("manualSelectionSection");

    if (!audienceMethod) return;

    function updateAudience() {

        if (audienceMethod.value === "smart") {

            smartFilters.style.display = "block";
            manualSelection.style.display = "none";

        } else {

            smartFilters.style.display = "none";
            manualSelection.style.display = "block";

        }

    }

    updateAudience();

    audienceMethod.addEventListener("change", updateAudience);

});

document.addEventListener("DOMContentLoaded", function () {

    const search = document.getElementById("clientSearch");

    if (!search) return;

    search.addEventListener("keyup", function () {

        const value = search.value.toLowerCase();

        document.querySelectorAll(".form-check").forEach(item => {

            const text = item.innerText.toLowerCase();

            item.style.display =
                text.includes(value)
                ? ""
                : "none";

        });

    });

});