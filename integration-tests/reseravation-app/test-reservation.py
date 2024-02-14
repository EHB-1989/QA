import unittest
from chambre import *
from reservation import *

class TestIntegrationPanierProduit(unittest.TestCase):
    c1 = Chambre(1,100)
    c2 = Chambre(2,200)
    c3 = Chambre(3,300)

    def test_reservation(self):
        res = Reservation(self.c1, 7 ,0)
        self.assertEqual(res.calculer_cout(),700)

    def test_annulation(self):
        c = Chambre(1,100)
        res = Reservation(c, 7 ,0)
        res.annuler(800)
        self.assertEqual(res.calculer_cout(),800)

if __name__ == '__main__':
    unittest.main()
