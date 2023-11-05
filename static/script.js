function toggleMenu() {
    var isSidebarOpen = sidebar.style.left === "0px" || sidebar.style.left === "";
    
    // Toggle the sidebar and change its visibility
    if (isSidebarOpen) {
        sidebar.style.left = "-250px";
        sidebar.style.visibility = "hidden";
    } else {
        sidebar.style.left = "0px";
        sidebar.style.visibility = "visible";
    }
    
    // Toggle the 'sidebar-open' class on the menuToggle element
    menuToggle.classList.toggle("sidebar-open", !isSidebarOpen);
    
    if (isSidebarOpen) {
        // Sidebar is open, hide the hamburger icon
        menuToggle.style.display = "none";
    } else {
        // Sidebar is closed, show the hamburger icon
        menuToggle.style.display = "block";
    }
    
    // Update the sidebar's transparency and backdrop filter based on its open/closed state
    if (isSidebarOpen) {
        sidebar.style.backgroundColor = "rgba(51, 51, 51, 0.8)";
        sidebar.style.backdropFilter = "blur(10px)";
    } else {
        sidebar.style.backgroundColor = "transparent";
        sidebar.style.backdropFilter = "none";
    }
}


