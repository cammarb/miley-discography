const selectBtn = document.getElementById("select-btn");
var open = false;

function toggleSelect() {
    var optionsContainer = document.getElementById("options-container");
    if (!open) {
        optionsContainer.style.display = "block";
        open = true;
    }
    else {
        optionsContainer.style.display = "none";
        open = false;
    }
};
