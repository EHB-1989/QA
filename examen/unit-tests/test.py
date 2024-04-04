import unittest
from app import Livre
from app import Bibliotheque

class TestLivre(unittest.TestCase) :
    def test_emprunt_livre(self) :
        l1 = Livre('Dragon ball Z', 'Akira Toriyama')
        l2 = Livre('One piece', 'Eichiro Oda')
        l3 = Livre('Metmorphose', 'Franz Kafka')
                 
        # test emprunt livre
        e1 = l1.emprunter()
        self.assertTrue(e1)
        
        e2 = l1.emprunter()
        self.assertFalse(e2)
        
    def test_retourner_livre(self) :        
        l1 = Livre('Dragon ball Z', 'Akira Toriyama')
        l2 = Livre('One piece', 'Eichiro Oda')
        l3 = Livre('Metmorphose', 'Franz Kafka')
        
        # test retourner livre
        l1.emprunter()
        
        r1 = l1.retourner()
        self.assertTrue(r1)
        
        r2 = l2.retourner()
        self.assertFalse(r2)
        
class TestBibliotheque(unittest.TestCase) :
    def test_ajout_livre(self) :
        biblio = Bibliotheque()
        
        l1 = Livre('Dragon ball Z', 'Akira Toriyama')
        l2 = Livre('One piece', 'Eichiro Oda')
        l3 = Livre('Metmorphose', 'Franz Kafka')
        
        # test ajout livre bibliotheque
        biblio.ajouter_livre(l1)
        self.assertEqual(len(biblio.livres),1)
        
        biblio.ajouter_livre(l2)
        biblio.ajouter_livre(l3)
        self.assertEqual(len(biblio.livres),3)
        
        
    def test_emprunt_livre(self) :
        biblio = Bibliotheque()
        
        l1 = Livre('Dragon ball Z', 'Akira Toriyama')
        l2 = Livre('One piece', 'Eichiro Oda')
        l3 = Livre('Metmorphose', 'Franz Kafka')
        
        biblio.ajouter_livre(l1)
        biblio.ajouter_livre(l2)
        biblio.ajouter_livre(l3)
                
        # test emprunt livre bibliotheque
        e1 = biblio.emprunter_livre('One piece')
        self.assertTrue(e1)
        
        e2 = biblio.emprunter_livre('One piece')
        self.assertFalse(e2)
        
        e3 = biblio.emprunter_livre('La peste')
        self.assertFalse(e3)
        
    def test_retourner_livre(self) :
        biblio = Bibliotheque()
        
        l1 = Livre('Dragon ball Z', 'Akira Toriyama')
        l2 = Livre('One piece', 'Eichiro Oda')
        l3 = Livre('Metmorphose', 'Franz Kafka')
        
        biblio.ajouter_livre(l1)
        biblio.ajouter_livre(l2)
        biblio.ajouter_livre(l3)
        
        # test retourner livre bibliotheque
        biblio.emprunter_livre('One piece')
        
        r1 = biblio.retourner_livre('One piece')
        self.assertTrue(r1)
        
        r2 = biblio.retourner_livre('One piece')
        self.assertFalse(r2)
        
        r3 = biblio.retourner_livre('La peste')
        self.assertFalse(r3)

if __name__ == '__main__' :
    unittest.main()
    