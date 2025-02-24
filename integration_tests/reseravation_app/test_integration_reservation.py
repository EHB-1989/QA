import unittest
from integration_tests.reseravation_app.reservation import Reservation
from integration_tests.reseravation_app.chambre import Chambre


class TestIntegrationReservation(unittest.TestCase):
    
    def test_creation_reservation(self):
        """Ici je vais essayer de vérifier que le coût de la réservation est bien calculé."""
        chambre = Chambre(numero=101, prix_base=100)
        reservation = Reservation(chambre, nb_nuits=4)
        self.assertEqual(reservation.calculer_cout(), 400, "Le coût total devrait être 400€ pour 4 nuits à 100€.")

    def test_promotion_reservation(self):
        """ Je vérifie l'application d'une promotion sur la réservation."""
        chambre = Chambre(numero=102, prix_base=200)
        reservation = Reservation(chambre, nb_nuits=2, promotion=10)
        self.assertEqual(reservation.calculer_cout(), 360, "Avec 10% de réduction, le coût devrait être 360€ au lieu de 400€.")

    def test_annulation_reservation_sans_frais(self):
        """Ici, je vérifie que l'annulation d'une réservation met le coût à 0."""
        chambre = Chambre(numero=103, prix_base=150)
        reservation = Reservation(chambre, nb_nuits=4)
        reservation.annuler(frais_annulation=0)
        self.assertEqual(reservation.calculer_cout(), 0, "Une réservation annulée sans frais doit coûter 0€.")

    def test_annulation_reservation_avec_frais(self):
        """Vérification qu'une annulation avec frais d'annulation applique le bon montant."""
        chambre = Chambre(numero=104, prix_base=100)
        reservation = Reservation(chambre, nb_nuits=5)
        frais_annulation = 50
        cout_apres_annulation = reservation.annuler(frais_annulation)
        self.assertEqual(cout_apres_annulation, 50, "Les frais d'annulation doivent être au minimum 50€.")

    def test_prix_saison(self):
        """Enfin, je vérifie la mise à jour du prix de la chambre selon la saison."""
        chambre = Chambre(numero=105, prix_base=120)
        chambre.definir_prix_saison(multiplicateur_saison=1.5) # +50%
        self.assertEqual(chambre.prix_saison, 180, "Le prix de la chambre doit être ajusté à 180€ en haute saison.")

        reservation = Reservation(chambre, nb_nuits=2)
        self.assertEqual(reservation.calculer_cout(), 360, "Avec un prix de saison de 180€, le coût pour 2 nuits devrait être 360€.")


if __name__ == '__main__':
    unittest.main()
