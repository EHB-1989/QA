import unittest

from chambre import Chambre

from reservation import Reservation

class testPanier(unittest.TestCase):
    def test(self):
        c1 = Chambre(1, 100)
        c4 = Chambre(4, 100)

        r1 = Reservation(c1, 3)
        r4 = Reservation(c4, 3)

        cout1, cout4 = 300,  300

        self.assertEqual(r1.calculer_cout(), cout1)
        self.assertEqual(r4.calculer_cout(), cout4)

        r4.annuler(0)

        cout4 = 0

        self.assertEqual(r4.calculer_cout(), cout4)
    
    def test2(self):   
        c2 = Chambre(2, 50)
        c3 = Chambre(3, 10)

        c2.definir_prix_saison(0.9)
        c3.definir_prix_saison(2)

        cout2, cout3 = 90, 40

        r2 = Reservation(c2, 2)
        r3 = Reservation(c3, 2)

        self.assertEqual(r2.calculer_cout(), cout2)
        self.assertEqual(r3.calculer_cout(), cout3)

        r3.annuler(10)
        cout3 += 10

        self.assertEqual(r3.calculer_cout(), cout3)


if __name__ == '__main__':
    unittest.main()