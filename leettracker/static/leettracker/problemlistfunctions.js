document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('filter-button').addEventListener('click', filterTable);
    document.getElementById('sort-button').addEventListener('click', sortTable);

    function filterTable() {
        var difficultyInput = document.getElementById('filter-difficulty').value;
        var solvedInput = document.getElementById('filter-solved').value;

        var table = document.getElementById('problems-table');
        var tr = table.getElementsByTagName('tr');

        for (var i = 1; i < tr.length; i++) {
            var tdDifficulty = tr[i].getElementsByTagName('td')[2];
            var tdSolved = tr[i].getElementsByTagName('td')[3];

            var difficultyText = tdDifficulty ? tdDifficulty.textContent || tdDifficulty.innerText : '';
            var solvedText = tdSolved ? tdSolved.textContent || tdSolved.innerText : '';

            var showRow = true;

            if (difficultyInput && difficultyText !== difficultyInput) {
                showRow = false;
            }

            if (solvedInput) {
                var solvedValue = solvedText.includes('✔') ? 'True' : 'False';
                if (solvedValue !== solvedInput) {
                    showRow = false;
                }
            }

            tr[i].style.display = showRow ? '' : 'none';
        }
    }

    function sortTable() {
        var sortOption = document.getElementById('sort-option').value;
        var table = document.getElementById('problems-table');
        var rows = Array.prototype.slice.call(table.getElementsByTagName('tr'), 1);
        var comparator;

        if (sortOption === 'number') {
            comparator = function(a, b) {
                return parseInt(a.getElementsByTagName('td')[0].innerText) - parseInt(b.getElementsByTagName('td')[0].innerText);
            };
        } else if (sortOption === 'name') {
            comparator = function(a, b) {
                return a.getElementsByTagName('td')[1].innerText.localeCompare(b.getElementsByTagName('td')[1].innerText);
            };
        }

        rows.sort(comparator);

        for (var i = 0; i < rows.length; i++) {
            table.getElementsByTagName('tbody')[0].appendChild(rows[i]);
        }
    }

    window.deleteProblem = function(problemId) {
        if (confirm('Are you sure you want to delete this problem?')) {
            fetch(`/problems/${problemId}/delete/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                }
            })
            .then(response => {
                if (response.ok) {
                    document.getElementById(`problem-${problemId}`).remove();
                } else {
                    alert('Failed to delete problem.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Failed to delete problem.');
            });
        }
    };
});