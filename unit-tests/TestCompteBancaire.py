from CompteBancaire import *
import unittest

class TestBancaire(unittest.TestCase):
    
    def test_get_solde(self):
        compte = CompteBancaire(20)
        
        assert compte.get_solde() ==20
        
    
    def test_depot(self):
        compte = CompteBancaire(50)
        montant = 50
        
        compte.depot(montant)
        
        assert compte.get_solde() == 100
        
    def test_retrait(self):
        compte = CompteBancaire(100)
        montant = 75
        
        compte.retrait(montant)
        
        assert compte.get_solde() == 25
        
            

if __name__ == "__main__":
    unittest.main()