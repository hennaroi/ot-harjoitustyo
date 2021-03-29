# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksen tarkoituksena on toimia turvallisena Blackjack-pelin harjoittelualustana, sillä pelissä ei pysty käyttämään oikeaa rahaa. 

## Käyttäjät
Sovelluksen ainoa käyttäjä on pelin *pelaaja*.

## Käyttöliittymäluonnos
Karkea ideointi käyttöliittymäluonnoksesta:
kuva
Sovellus aukeaa panosnäkymään, jossa asetetaan panos. Panoksen asettamisen jälkeen päästään pelinäkymään, jossa itse peli tapahtuu.

## Perusversion tarjoama toiminnallisuus
### Panosnäkymä
- asetetaan panos, joka on pienimmillään 10€ ja suurimmillaan 1000€
- panos muodostuu pelimerkeistä 1, 5, 10, 50, 100 ja 500 sekä näiden summista
- kun pelaaja on valmis, siirrytään _pelinäkymään_
### Pelinäkymä
- pelaajan rahavarastosta vähennetään panos
- jakaja jakaa ensin pelaajalle kortin, sitten itselleen kortin ja sen jälkeen vielä yhden kortin pelaajalle, kaikki kuvapuoli ylöspäin
- pelaaja valitsee valikosta: 
  - _LISÄÄ_: pelaaja saa uuden kortin
    - jos summa on 9-11 -> _JÄÄ / LISÄÄ / TUPLAUS_
    - jos summa on alle 8 tai yli 12 mutta alle 21 -> _JÄÄ / LISÄÄ_
    - jos summa on 21 -> pelaaja on voittanut ja saa panoksensa kaksinkertaisena takaisin -> _panosnäkymä_
    - jos summa on yli 21 -> pelaaja on hävinnyt -> _panosnäkymä_
  - _JÄÄ_: pelaaja jää nykyiseen tilanteeseen ja vuoro siirtyy jakajalle
    - jakaja saa nostaa kortteja niin kauan, kunnes niiden summa on yli 16
      - jos summa on molemmilla 21 -> pelaaja on voittanut ja saa panoksensa kaksinkertaisena takaisin -> _panosnäkymä_
      - jos jakajalla on summa 21 ja pelaajalla alle 21 -> pelaaja on hävinnyt -> _panosnäkymä_
      - jos jakajan summa on suurempi kuin pelaajan summa -> pelaaja on hävinnyt -> _panosnäkymä_
      - jos jakajan summa on pienempi kuin pelaajan summa -> pelaaja on voittanut ja saa panoksensa kaksinkertaisena takaisin -> _panosnäkymä_
      - jos jakajalla ja pelaajalla on sama summa -> pelaaja on hävinnyt -> _panosnäkymä_
  - _TUPLAUS_: mahdollista vain, jos korttien summa on 9-11 -> pelaaja saa vain yhden kortin lisää -> vuoro siirtyy jakajalle eli siirrytään tilanteeseen _JÄÄ_
  - _ANTAUDU_: pelaaja häviää puolet panoksestaan, mutta saa toisen puolikkaan -> _panosnäkymä_

- kaikki numerokortit 2, 3, 4, 5, 6, 7, 8 ja 9 ovat oman numeronsa arvoisia
- kirjainkortit J, Q ja K ovat 10 arvoisia
- kirjainkortti A on joko 1 tai 11 arvoinen, mutta tämä jää kortin saaneelle osapuolelle päätettäväksi

## Jatkokehitysideoita
ideoita
