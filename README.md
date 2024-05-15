
# Dev-Challenge

Il progetto è nato da una "sfida di sviluppo" con l'obbiettivo di stimare alcune mie abilità tecniche; consiste nella realizzazione di un'applicazione web che funge da calcolatrice online. Gli utenti possono inserire espressioni aritmetiche nella pagina web e ottenerne il risultato.
Ps. Il progetto è stato successivamente riutilizzato per compiere ulteriori operazioni di stima con istruzioni non presenti sulla consegna.

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
├── .gitignore
├── app.py
├── dev-challenge.pdf
├── README.md
├── requirements.txt
└── start.sh

3 directories, 10 files
```
-   `app.py`: Il file principale del server web.
-   `index.html`: Il template della pagina web.
-   `style.css`: Il foglio di stile per la pagina web.
-   `script.js`: Lo script JavaScript per gestire le interazioni utente e le richieste al server.
-   `dev-challenge.pdf`: La consegna iniziare assegnatami.
-   `start.sh`: Script di avvio del server.

## Avvio del server
  Per avviare il server è necessario scaricare il codice sorgente del progetto ed estrarlo.
  Aprire un terminale nella cartella del progetto ed eseguire il seguente comando: `chmod +x start.sh && ./start.sh`