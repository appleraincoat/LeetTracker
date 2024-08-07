function initializeDropdown() {
    const dropdownBox = document.getElementById('topics-dropdown-box');
    const dropdownContent = document.getElementById('topics-dropdown-content');

    if (dropdownBox && dropdownContent) {
        dropdownBox.addEventListener('click', function() {
            dropdownContent.classList.toggle('show');
        });

        window.addEventListener('click', function(event) {
            if (!event.target.closest('#topics-dropdown-box')) {
                if (dropdownContent.classList.contains('show')) {
                    dropdownContent.classList.remove('show');
                }
            }
        });
    }
}

document.addEventListener('DOMContentLoaded', function() {
    initializeDropdown();
});