# kirja-arvostelut

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan arvosteluja tietyistä kirjoista.
- Käyttäjä näkee sovellukseen sekä itse lisäämänsä että muiden käyttäjien lisäämät arvostelut.
- Käyttäjä pystyy etsimään arvosteluja hakusanalla.
- Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä arvosteluja.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät arvostelut.
- Käyttäjä pystyy valitsemaan arvostelulle yhden tai useamman luokittelun (esim. kirjan lajityyppi ja arvosana).
- Käyttäjä pystyy kirjoittamaan arvosteluja kirjoista.

# Sovelluksen testaaminen paikallisesti

1. Luo tietokanta

Aja projektikansiossa:
sqlite3 database.db < schema.sql 

- Tämä luo tiedoston database.db paikalliseen projektiin

2. Käynnistä sovellus

Linux/macOS:
export FLASK_APP=app.py 
flask run

Windows:
set FLASK_APP=app.py
flask run

3. Sovelluksen avaaminen selaimessa 
Sovellus käynnistyy myös paikallisesti osoitteessa: http://127.0.0.1:5000

4. Sovelluksen testaaminen

- Käyttäjien luominen, sisään- ja uloskirjautuminen
- Kirja-arvostelujen lisääminen, muokkaaminen ja poistaminen
- Hakutoimintojen testaaminen
