document.addEventListener("DOMContentLoaded", function () {
    const analyzeButton = document.getElementById("location-button");
    const settingsButton = document.getElementById("bType-button");

    analyzeButton.addEventListener("click", function () {
        alert("Searching by Location...");
    });

    settingsButton.addEventListener("click", function () {
        alert("Searching by Business Information...");
    });
});
