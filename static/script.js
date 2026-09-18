document.addEventListener("DOMContentLoaded", function () {

    const inputs = document.querySelectorAll(
        "input, select"
    );

    inputs.forEach(function (input) {

        input.addEventListener("focus", function () {

            this.style.transform = "scale(1.01)";

        });

        input.addEventListener("blur", function () {

            this.style.transform = "scale(1)";

        });

    });


    const buttons = document.querySelectorAll(
        "button"
    );

    buttons.forEach(function (button) {

        button.addEventListener("click", function () {

            this.style.transform = "scale(0.98)";

            setTimeout(() => {

                this.style.transform = "";

            }, 100);

        });

    });

});