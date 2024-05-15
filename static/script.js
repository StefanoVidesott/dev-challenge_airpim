function calculate() {
    // Extract the expression entered by the user
    var expression = document.getElementById('expression').value;
    // Send a POST request to the server
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', // Corrected content type
        },
        body: JSON.stringify({ expression: expression }) // Convert data to JSON format
    })
    // Handle the server response
    .then(response => response.json())
    .then(data => {
        // Extract HTML elements for the result and history
        var resultElement = document.getElementById('result');
        // If the result is a syntax error, color the result red
        if (data.status === 'error') {
            resultElement.innerHTML = 'Result: <span style="color: red;">' + data.error_type + '</span>';
            return;
        }
        // Otherwise, color the result green
        if (data.status === 'success') {
            var historyElement = document.getElementById('history');
            resultElement.innerHTML = 'Risultato: <span style="color: green;">' + data.result + '</span>';
            historyElement.innerHTML += '<p>' + expression + ' = ' + '<span style="color: green;">' + data.result + '</span></p>';
        }
        // If the server returns an unknown state, color the result red
        else {
            resultElement.innerHTML = 'Result: <span style="color: red;">Unknown status</span>';
        }
    })
    .catch(error => console.error('Errore:', error));
    console.log('Request sent to server');
}

function clear_history() {
    // Clear the history
    var historyElement = document.getElementById('history');
    var resultElement = document.getElementById('result');
    historyElement.innerHTML = '';
    resultElement.innerHTML = 'Result:';
    console.log('History cleared');

    fetch('/clear_history', {
        method: 'POST'
    })
}