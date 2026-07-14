// document.addEventListener("DOMContentLoaded", function () {

//     const generateBtn = document.getElementById("generateBtn");
//     const loading = document.getElementById("loadingMessage");
//     const result = document.getElementById("aiResult");

//     if (!generateBtn) return;

//     generateBtn.addEventListener("click", function () {

//         generateBtn.disabled = true;

//         generateBtn.innerHTML =
//             '<span class="spinner-border spinner-border-sm me-2"></span>Generating...';

//         loading.style.display = "block";

//         result.style.display = "none";

//         setTimeout(function () {

//             loading.style.display = "none";

//             result.style.display = "flex";

//             generateBtn.disabled = false;

//             generateBtn.innerHTML =
//                 '<i class="bi bi-stars me-2"></i>Generate';

//         }, 2000);

//     });

// });

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

// Audience Selection

const audienceMethod = document.getElementById("audienceMethod");

const smartFilters = document.getElementById("smartFilters");

const manualSelection = document.getElementById("manualSelection");

const aiPromptSection = document.getElementById("aiPromptSection");

if(audienceMethod){

    function updateAudience(){

        smartFilters.style.display="none";

        manualSelection.style.display="none";

        aiPromptSection.style.display="none";

        if(audienceMethod.value==="Smart Filters"){

            smartFilters.style.display="block";

        }

        else if(audienceMethod.value==="Manual Client Selection"){

            manualSelection.style.display="block";

        }

        else{

            aiPromptSection.style.display="block";

        }

    }

    updateAudience();

    audienceMethod.addEventListener("change",updateAudience);

}