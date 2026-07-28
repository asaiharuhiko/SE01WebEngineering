const button = document.getElementById("sidebar-toggle");

if (button) {
    if (localStorage.getItem("sidebar") === "closed") {
        document.body.classList.add("sidebar-closed");
    }

    button.addEventListener("click", () => {
        document.body.classList.toggle("sidebar-closed");

        localStorage.setItem(
            "sidebar",
            document.body.classList.contains("sidebar-closed")
                ? "closed"
                : "open"
        );
    });
}