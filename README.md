# kirja-arvostelut

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan arvosteluja tietyistä kirjoista.
- Käyttäjä näkee sovellukseen sekä itse lisäämänsä että muiden käyttäjien lisäämät arvostelut.
- Käyttäjä pystyy etsimään arvosteluja hakusanalla.
- Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä arvosteluja.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät arvostelut.
- Käyttäjä pystyy valitsemaan arvostelulle yhden tai useamman luokittelun (esim. kirjan lajityyppi ja arvosana).
- Käyttäjä pystyy kirjoittamaan arvosteluja kirjoista.

Kirja-arvostelu sovelluksessa käyttäjät voivat lisätä ja lukea muiden tekemiä kirja-arvosteluja tietyistä kirjoista. Sovelluksessa käyttäjillä on omat profiilit, ja arvosteluja voi luokitella kirjan lajityypin ja arvostanan mukaan.

# Sovelluksen testaaminen

1. Luo tietokanta

Aja seuraava komento projektikansiossa:
```bash
sqlite3 database.db < schema.sql

2. Käynnistä sovellus

Linux/macOS:
```bash
export FLASK_APP=app.py 
flask run

Windows:
```bash
set FLASK_APP=app.py
flask run

3. Avaa sovellus selaimessa
- Sovellus käynnistyy osoitteessa: http://127.0.0.1:5000
