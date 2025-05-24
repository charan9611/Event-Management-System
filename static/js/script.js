document.getElementById("hamburger").addEventListener("click", function() {
    document.querySelector(".nav-bar ul").classList.toggle("show");
});


function toggleDropdown() {
    const dropdown = document.getElementById("dropdownContent");
    dropdown.classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        const dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
            dropdowns[i].classList.remove('show');
        }
    }
}



