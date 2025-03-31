function createWork() {
    console.log("created")
    let company = document.getElementById('company').value
    let term = document.getElementById('term').value

    fetch('/work', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'company': company || 'empty', 'term': term || '0'})
    })
    .then(response => {
        if (response.ok) {
            location.reload();
        }
    })
}

function clearEverything() {
    if (confirm('Are you sure you want to clear all records?')) {
        fetch('/clear', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
        })
        .then(response => {
            if (response.ok) {
                location.reload();
            }
        })
    }
}