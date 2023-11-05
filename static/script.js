document.addEventListener("DOMContentLoaded", function () {
    const analyzeButton = document.getElementById("analyze-button");
    const settingsButton = document.getElementById("settings-button");

    analyzeButton.addEventListener("click", function () {
        alert("Analyzing data...");
    });

    settingsButton.addEventListener("click", function () {
        alert("Opening settings...");
    });
});
