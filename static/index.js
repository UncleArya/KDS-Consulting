// Dynamic year setting
const date = new Date();
let currentYear = date.getFullYear();
document.querySelector("#website-date").innerText = currentYear;

// Change active tab in Navbar
document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.href === window.location.href) {
        link.classList.add("active");
        link.setAttribute("aria-current", "page");
    }
});
