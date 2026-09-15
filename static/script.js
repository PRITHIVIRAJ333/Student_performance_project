document.addEventListener("DOMContentLoaded", function () {

    const inputs = document.querySelectorAll("input");

    inputs.forEach(function (input) {

        input.addEventListener("focus", function () {
            this.style.transform = "scale(1.01)";
        });

        input.addEventListener("blur", function () {
            this.style.transform = "scale(1)";
        });

    });

});