# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksen tarkoituksena on toimia turvallisena Blackjack-pelin harjoittelualustana, sillä pelissä ei pysty käyttämään oikeaa rahaa. Pelin tavoitteena on saada korttien avulla summa 21 tai päästä mahdollisimman lähelle sitä kuitenkin ylittämättä summaa 21, jollon pelaajalla on suurin todennäköisyys voittaa jakajan käsi ja saada pelin alussa asettama panos kaksinkertaisena takaisin.

## Käyttäjät
Sovelluksen ainoa käyttäjä on pelin *pelaaja*.

## Käyttöliittymäluonnos
Karkea ideointi käyttöliittymäluonnoksesta:

<img src="https://github.com/hennaroi/ot-harjoitustyo/blob/master/dokumentaatio/K%C3%A4ytt%C3%B6liittym%C3%A4luonnos.jpg"  width="600">

Sovellus aukeaa panosnäkymään, jossa asetetaan panos. Panoksen asettamisen jälkeen päästään pelinäkymään, jossa itse peli tapahtuu. Pelin yläreunassa näkyy pelaajan rahatilanne, ja ehkä mahdollisesti myös voittoprosentti.

## Perusversion tarjoama toiminnallisuus
Pelaajalle annetaan alussa 1000€. Jos pelaajalta loppuu rahat, niin tälle annetaan uudestaan 1000€.
### Panosnäkymä
- asetetaan panos, joka on pienimmillään 10€ ja suurimmillaan 1000€
- panos muodostuu pelimerkeistä 1, 5, 10, 50, 100 ja 500 sekä näiden summista
- kun pelaaja on valmis, siirrytään __pelinäkymään__
### Pelinäkymä
- pelaajan rahavarastosta vähennetään panos
- jakaja jakaa ensin pelaajalle kortin, sitten itselleen kortin ja sen jälkeen vielä yhden kortin pelaajalle, kaikki kuvapuoli ylöspäin
- pelaaja valitsee valikosta: 
  - __LISÄÄ__: pelaaja saa uuden kortin,minkä jälkeen:
    - jos summa on 9-11 -> __JÄÄ / LISÄÄ / TUPLAUS__
    - jos summa on alle 8 tai yli 12 mutta alle 21 -> __JÄÄ / LISÄÄ__
    - jos summa on 21 -> __JÄÄ__
    - jos summa on yli 21 -> pelaaja on hävinnyt -> __panosnäkymä__
  - __JÄÄ__: pelaaja jää nykyiseen tilanteeseen ja vuoro siirtyy jakajalle:
    - jakaja nostaa kortteja niin kauan, kunnes niiden summa on yli 16
      - jos jakajan summa on yli 21 -> pelaaja on voittanut ja saa panoksensa kaksinkertaisena takaisin -> __panosnäkymä__
      - jos summa on molemmilla 21 
        - jos pelaaja on saanut kahdella ensimmäisellä kortillaan summan 21 -> blackjack -> pelaaja on voittanut ja saa panoksensa kaksinkertaisena takaisin -> __panosnäkymä__
        - jos jakaja on saanut kahdella ensimmäisellä kortillaan summan 21 -> blackjack -> pelaaja on hävinnyt -> __panosnäkymä__
        - jos pelaajalla on vähemmän kortteja kuin jakajalla -> pelaaja on voittanut ja saa panoksensa kaksinkertaisena takaisin -> __panosnäkymä__
        - jos jakajalla on vähemmän kortteja kuin pelaajalla -> pelaaja on hävinnyt -> __panosnäkymä__
      - jos jakajalla on summa 21 ja pelaajalla alle 21 -> pelaaja on hävinnyt -> __panosnäkymä__
      - jos jakajan summa on suurempi kuin pelaajan summa -> pelaaja on hävinnyt -> __panosnäkymä__
      - jos jakajan summa on pienempi kuin pelaajan summa -> pelaaja on voittanut ja saa panoksensa kaksinkertaisena takaisin -> __panosnäkymä__
      - jos jakajalla ja pelaajalla on sama summa -> pelaaja on hävinnyt -> __panosnäkymä__
  - __TUPLAUS__: mahdollista vain, jos korttien summa on 9-11 -> pelaaja saa vain yhden kortin lisää -> vuoro siirtyy jakajalle eli siirrytään tilanteeseen __JÄÄ__
  - __ANTAUDU__: 
    - mahdollista vain heti korttien jaon jälkeen
    - pelaaja häviää puolet panoksestaan, mutta saa toisen puolikkaan -> __panosnäkymä__


- kaikki numerokortit 2, 3, 4, 5, 6, 7, 8 ja 9 ovat oman numeronsa arvoisia
- kirjainkortit J, Q ja K ovat 10 arvoisia
- kirjainkortti A on joko 1 tai 11 arvoinen, mutta tämä jää kortin saaneelle osapuolelle päätettäväksi

## Jatkokehitysideoita
- pelaajien määrän lisääminen siten, että monta pelaajaa pystyy pelaamaan samaa jakajaa vastaan
- lisää toiminnallisuuksia:
  - __jakaminen__: jos pelaajan kaksi ensimmäistä korttia ovat saman arvoiset, pelaaja voi halutessan jakaa kortit kahdeksi eri kädeksi, mutta tällöin pelaajan on myös tuplattava panoksensa ja jaettava se tasan näiden kahden käden kesken 
  - __vakuutus__: jos jakajan ensimmäinen kortti on ässä, pelaaja voi halutessaan vakuuttaa kätensä, vakuus on yleensä puolet panoksesta
    - jos jakajan saa seuraavalla kortilla summan 21 -> pelaaja pitää panoksensa eli ei voita eikä häviä mitään
    - jos jakajan ei saa seuraavalla kortilla summaa 21 -> pelaaja häviää vakuutensa ja peli jatkuu normaalisti
  - __tasaraha__: jos jakajan ensimmäinen kortti on ässä ja pelaajalla on blackjack, pelaaja voi halutessaan pyytää tasarahan
    - tällöin pelaaja on voittanut 
    - jos pelaaja ei halunnut tasarahaa ja jakaja saa blackjackin -> panokset palautetaan
