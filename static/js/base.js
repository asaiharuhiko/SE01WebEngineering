const button = document.getElementById("sidebar-toggle");
const overlay = document.getElementById("sidebar-overlay");

function isMobile() {
    return window.matchMedia("(max-width: 768px)").matches;
}

function closeSidebar() {
    document.body.classList.remove("sidebar-open", "sidebar-closed");
}

function toggleSidebar() {
    if (isMobile()) {
        document.body.classList.toggle("sidebar-open");
    } else {
        document.body.classList.toggle("sidebar-closed");
        localStorage.setItem(
            "sidebar",
            document.body.classList.contains("sidebar-closed")
                ? "closed"
                : "open"
        );
    }
}

if (button) {
    if (!isMobile() && localStorage.getItem("sidebar") === "closed") {
        document.body.classList.add("sidebar-closed");
    }

    button.addEventListener("click", toggleSidebar);

    window.addEventListener("resize", () => {
        if (!isMobile()) {
            document.body.classList.remove("sidebar-open");
        }
    });
}

if (overlay) {
    overlay.addEventListener("click", closeSidebar);
}