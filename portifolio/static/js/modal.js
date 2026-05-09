const modal = document.getElementById("email-modal");

const openBtn = document.getElementById("open-email-modal");

const closeBtn = document.getElementById("close-email-modal");


openBtn.addEventListener("click", function(event) {

    event.preventDefault();

    modal.classList.add("active");

});


closeBtn.addEventListener("click", function() {

    modal.classList.remove("active");

});


window.addEventListener("click", function(event) {

    if (event.target === modal) {

        modal.classList.remove("active");

    }

});

