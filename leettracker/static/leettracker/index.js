document.addEventListener('DOMContentLoaded', function() {
    const randomProblemBtn = document.getElementById('random-problem-btn');
    if (randomProblemBtn) {
        randomProblemBtn.addEventListener('click', function() {
            fetch(randomProblemUrl)
                .then(response => response.text())
                .then(html => {
                    document.getElementById('random-problem-display').innerHTML = html;
                    initializeDropdown();  // Re-initialize dropdown if new content is loaded
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('random-problem-display').innerHTML = `<p>Error fetching problem.</p>`;
                });
        });
    }

    initializeDropdown();
});