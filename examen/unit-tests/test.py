import unittest
from app import Livre, Bibliotheque

class TestLivre(unittest.TestCase):    
    def test_emprunter(self):
        l = Livre('Fairy Tail', 'Hiro Mashima')
        
        self.assertFalse(l.est_emprunte)
        
        emprunter1 = l.emprunter()
                
        self.assertTrue(emprunter1)
        self.assertTrue(l.est_emprunte)
        
        emprunte2 = l.emprunter()
        
        self.assertFalse(emprunte2)
        self.assertTrue(l.est_emprunte)
    
    def test_retourner(self):
        l = Livre('Fairy Tail', 'Hiro Mashima')
        
        self.assertFalse(l.est_emprunte)
        
        l.emprunter()
        retourne1 = l.retourner()
                
        self.assertTrue(retourne1)
        self.assertFalse(l.est_emprunte)
        
        retourne2 = l.retourner()
        
        self.assertFalse(retourne2)
        self.assertFalse(l.est_emprunte)

class TestBibliotheque(unittest.TestCase):    
    def test_ajouter_livre(self):
        b = Bibliotheque()
        l1 = Livre('Fairy Tail', 'Hiro Mashima')
        l2 = Livre('My Hero Academia', 'Kohei Horikoshi')
        l3 = Livre('The Promised Neverland', 'Posuka Demisu')
        
        b.ajouter_livre(l1)
        b.ajouter_livre(l2)
        
        self.assertEqual(len(b.livres), 2)
        self.assertEqual(b.livres[0].titre, 'Fairy Tail')
        self.assertEqual(b.livres[0].auteur, 'Hiro Mashima')
        
        b.ajouter_livre(l3)
        
        self.assertEqual(len(b.livres), 3)
        
        b.ajouter_livre('Je suis un livre')
        
        self.assertEqual(len(b.livres), 4)
                
    def test_emprunter_livre(self):
        b = Bibliotheque()
        l1 = Livre('Fairy Tail', 'Hiro Mashima')
        
        b.ajouter_livre(l1)
        
        emprunte1 = b.emprunter_livre('Fairy Tail')
        
        self.assertTrue(emprunte1)
        self.assertTrue(l1.est_emprunte)
        
        emprunte2 = b.emprunter_livre('Fairy Tail')
        
        self.assertFalse(emprunte2)
        self.assertTrue(l1.est_emprunte)
        
        emprunte3 = b.emprunter_livre('My Hero Academia')
        
        self.assertFalse(emprunte3)
    
    def test_retourner_livre(self):
        b = Bibliotheque()
        l1 = Livre('Fairy Tail', 'Hiro Mashima')
        
        b.ajouter_livre(l1)
        
        b.emprunter_livre('Fairy Tail')
    
        self.assertTrue(l1.est_emprunte)
        
        retourne1 = b.retourner_livre('Fairy Tail')
        
        self.assertTrue(retourne1)
        self.assertFalse(l1.est_emprunte)
        
        retourne2 = b.retourner_livre('Fairy Tail')
        
        self.assertFalse(retourne2)
        self.assertFalse(l1.est_emprunte)
        
        retourne3 = b.retourner_livre('My Hero Academia')
        
        self.assertFalse(retourne3)
     
if __name__ == '__main__':
    unittest.main()             


    