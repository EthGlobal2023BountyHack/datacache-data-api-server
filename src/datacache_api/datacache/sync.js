function syncTagsForId(event, url) {
    event.preventDefault();
    fetch(url, { method: 'POST' })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            alert('Tags synced successfully.');
        })
        .catch(error => {
            console.log('There was a problem with the fetch operation:', error.message);
        });
}