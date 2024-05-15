
# Dev-Challenge

Il progetto è nato da una "sfida di sviluppo" con l'obbiettivo di stimare alcune mie abilità tecniche; consiste nella realizzazione di un'applicazione web che funge da calcolatrice online. Gli utenti possono inserire espressioni aritmetiche nella pagina web e ottenerne il risultato.
Ps. Il progetto è stato successivamente riutilizzato per compiere ulteriori operazioni di stima con istruzioni non presenti sulla consegna.
    
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