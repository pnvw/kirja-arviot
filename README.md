# kirja-arvostelut

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan arvosteluja tietyistä kirjoista.
- Käyttäjä näkee sovellukseen sekä itse lisäämänsä että muiden käyttäjien lisäämät arvostelut.
- Käyttäjä pystyy etsimään arvosteluja hakusanalla.
- Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä arvosteluja.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät arvostelut.
- Käyttäjä pystyy valitsemaan arvostelulle yhden tai useamman luokittelun (esim. kirjan lajityyppi ja arvosana).
- Käyttäjä pystyy kirjoittamaan arvosteluja kirjoista.

Kirja-arvostelusovelluksessa käyttäjät voivat lisätä ja lukea muiden tekemiä kirja-arvosteluja tietyistä kirjoista. Sovelluksessa käyttäjillä on omat profiilit, ja arvosteluja voi luokitella kirjan lajityypin ja arvosanan mukaan.

# Sovelluksen asennus

Asenna flask-kirjasto:
```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:
```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:
```
@ flask run
```
