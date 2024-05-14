
# Dev-Challenge

Il progetto è nato da una "sfida di sviluppo" con l'obbiettivo di stimare alcune mie abilità tecniche; consiste nella realizzazione di un'applicazione web che funge da calcolatrice online. Gli utenti possono inserire espressioni aritmetiche nella pagina web e ottenerne il risultato.

## Istruzioni per l'esecuzione

-   Come avviare il server:
1.  Aprire il terminale e spostarsi nella directory principale del progetto
2. Avviare il server eseguendo il seguente comando `python app.py start`
(`python app.py --help` per maggiori informazioni) 
4. Apri il browser e vai all'indirizzo http://localhost:8000 per utilizzare la calcolatrice.
    

## Struttura del Progetto

```
.
├── resources
│   └── favicon.ico
├── static
│   ├── script.js
│   └── style.css
├── templates
│   └── index.html
├── app.py
├── Dockerfile
└── README.md

3 directories, 7 files
```
-   `app.py`: Il file principale del server web. Contiene la logica per gestire le richieste HTTP e calcolare le espressioni aritmetiche.
-   `index.html`: La pagina web della calcolatrice.
-   `style.css`: Il foglio di stile per la pagina web.
-   `script.js`: Lo script JavaScript per gestire le interazioni utente e le richieste al server.

## Funzionalità
-  Il server dispone della possibilità di selezionare la porta tramite apposito argomento all'avvio.
(`python app.py start --port <PORT_NUMBER>`)
-   Gli utenti possono inserire espressioni aritmetiche nel campo di input e premere il pulsante "CALCOLA" per ottenere il risultato.
-   Il server valuta l'espressione aritmetica e restituisce il risultato in formato JSON.
-   Gli errori di sintassi nell'espressione aritmetica vengono gestiti e restituiti agli utenti.

## Docker
-   Nel progetto è anche presente un `Dockerfile` che simula il progetto in un ambiente con installato python 3.9. 
  Per avviare il progetto tramite Docker è sufficente eseguire i sguenti comandi nella sua directory principale.
1. `docker build -t dev-challenge .`
2. `sudo docker run -it --rm -p 8000:8000 dev-challenge`