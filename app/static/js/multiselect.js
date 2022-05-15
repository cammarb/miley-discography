let expanded = false;

const showCheckboxes = () => {
    const checkboxes = document.getElementById("checkboxes");
    if (!expanded) {
        checkboxes.style.display = "block";
        expanded = true;
    } else {
        checkboxes.style.display = "none";
        expanded = false;
    }
}

const selectBox = document.querySelector('.selectBox')
selectBox.addEventListener('click', showCheckboxes)