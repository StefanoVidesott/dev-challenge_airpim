function calculate() {
    // Estrae l'espressione inserita dall'utente
    var expression = document.getElementById('expression').value;
    // Invia la richiesta POST al server
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'expression=' + encodeURIComponent(expression)
    })
    // Gestisce la risposta del server
    .then(response => response.json())
    .then(data => {
        // Estrae gli elementi HTML per il risultato e la storia
        var resultElement = document.getElementById('result');
        // Se il risultato è un errore di sintassi, colora di rosso il risultato
        if(data.status === 'error') {
            resultElement.innerHTML = 'Risultato: <span style="color: red;">' + data.error_type + '</span>';
            return;
        }
        // Altrimenti colora di verde il risultato
        if(data.status === 'success') {

            var historyElement = document.getElementById('history');
            resultElement.innerHTML = 'Risultato: <span style="color: green;">' + data.result + '</span>';
            historyElement.innerHTML += '<p>' + expression + ' = ' + '<span style="color: green;">' + data.result + '</span></p>';

        }   
        // Se il server restituisce uno stato sconosciuto, colora di rosso il risultato
        else {
            resultElement.innerHTML = 'Risultato: <span style="color: red;">Stato sconosciuto</span>';
        }
    })
    .catch(error => console.error('Errore:', error));
    console.log('Richiesta inviata');
}
