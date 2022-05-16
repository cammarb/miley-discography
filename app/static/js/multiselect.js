var openArtist = false;
var openFeaturing = false;

function toggleArtist() {
    var optionsContainer = document.getElementById("artist-container");
    if (!openArtist) {
        optionsContainer.style.display = "block";
        openArtist = true;
    }
    else {
        optionsContainer.style.display = "none";
        openArtist = false;
    }
};

function toggleFeaturing() {
    var optionsContainer = document.getElementById("featuring-container");
    if (!openFeaturing) {
        optionsContainer.style.display = "block";
        openFeaturing = true;
    }
    else {
        optionsContainer.style.display = "none";
        openFeaturing = false;
    }
};
