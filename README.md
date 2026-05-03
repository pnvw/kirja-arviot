# Kirja-arvostelut

## Sovelluksen toiminnot

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan arvosteluja tietyistä kirjoista.
- Käyttäjä näkee sovellukseen sekä itse lisäämänsä että muiden käyttäjien lisäämät arvostelut.
- Käyttäjä pystyy etsimään arvosteluja hakusanalla.
- Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä arvosteluja.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät arvostelut.
- Käyttäjä pystyy luokitella arvostelun kirjan genren ja kohderyhmän mukaan.

Kirja-arvostelusovelluksessa käyttäjät voivat lisätä, lukea ja kommentoida muiden tekemiä kirja-arvosteluja tietyistä kirjoista. Sovelluksessa käyttäjillä on omat profiilit, ja arvosteluja voi luokitella kirjan genren ja kohderyhmän mukaan.

## Sovelluksen asennus

Asenna **`flask`**-kirjasto:
```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:
```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Sovelluksen käynnistys:
```
@ flask run
```
