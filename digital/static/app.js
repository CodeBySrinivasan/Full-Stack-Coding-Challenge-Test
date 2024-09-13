document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent the default form submission

        const formData = new FormData(form);

        fetch('/api/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Process the response data and display it
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '<h2>Results:</h2>';

            data.forEach(item => {
                const p = document.createElement('p');
                p.textContent = `${item.Employee_Name} (Email: ${item.Employee_EmailID}) will give a gift to ${item.Secret_Child_Name} (Email: ${item.Secret_Child_EmailID})`;
                resultsDiv.appendChild(p);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
