import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahamaara_ja_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_kassan_rahamaara_kasvaa_edullisen_lounaan_hinnalla_ja_vaihtoraha_on_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1240)
        
    def test_kassan_rahamaara_kasvaa_maukkaan_lounaan_hinnalla_ja_vaihtoraha_on_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1400)
        
    def test_kateisella_myytyjen_edullisten_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisella_myytyjen_maukkaiden_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_edullisen_maksu_kateisella_ei_ole_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_maukkaan_maksu_kateisella_ei_ole_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_kortilla_tarpeeksi_rahaa_edulliseen(self):
        self.maksukortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "saldo: 2.6")
        
    def test_kortilla_tarpeeksi_rahaa_maukkaaseen(self):
        self.maksukortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        
    def test_kortilla_myytyjen_edullisten_lounaiden_maara_kasvaa(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_kortilla_myytyjen_maukkaiden_lounaiden_maara_kasvaa(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kortilla_ei_tarpeeksi_rahaa_edulliseen(self):
        self.maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_kortilla_ei_tarpeeksi_rahaa_maukkaaseen(self):
        self.maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kortilla_edullista_maksettaessa_kassan_rahamaara_ei_muutu(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000)
    
    def test_kortilla_maukasta_maksettaessa_kassan_rahamaara_ei_muutu(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000)
        
    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassan_rahamaara_kasvaa(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1100)
    
    def test_kortille_ladattava_rahamaara_on_positiivinen(self):
        self.maksukortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100), None)
