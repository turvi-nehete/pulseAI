document.addEventListener("DOMContentLoaded", function () {

    const calendarEl = document.getElementById("calendar");

    if (!calendarEl) return;

    const calendar = new FullCalendar.Calendar(calendarEl, {

        initialView: "dayGridMonth",

        height: 500,

        headerToolbar: {

            left: "prev,next today",

            center: "title",

            right: ""

        },

        events: [

    {
        title: "Regional Sales Review Meeting",
        start: "2026-07-10"
    },

    {
        title: "Distributor Follow-up Meeting",
        start: "2026-07-12"
    }

],
eventClick: function(info){

    info.jsEvent.preventDefault();

    info.el.style.whiteSpace = "normal";
    info.el.style.height = "auto";
    info.el.style.zIndex = "999";

}

    });

    calendar.render();

});