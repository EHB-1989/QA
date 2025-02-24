import pytest
from reservation import Reservation
from chambre import Chambre

def test_calculer_cout_sans_promotion():
    """Test du calcul du coût sans promotion."""
    chambre = Chambre(101, 100)  # Prix de base : 100€/nuit
    reservation = Reservation(chambre, 3)  # 3 nuits
    assert reservation.calculer_cout() == 300, "Le coût devrait être 300€"

def test_calculer_cout_avec_promotion():
    """Test du calcul du coût avec une promotion."""
    chambre = Chambre(102, 200)  # Prix de base : 200€/nuit
    reservation = Reservation(chambre, 2, promotion=10)  # 10% de réduction
    assert reservation.calculer_cout() == 360, "Le coût devrait être 360€ avec la promo"

def test_annulation_sans_frais():
    """Test de l'annulation sans frais d'annulation."""
    chambre = Chambre(103, 150)
    reservation = Reservation(chambre, 4)
    reservation.annuler(frais_annulation=0)
    assert reservation.calculer_cout() == 0, "Une réservation annulée doit avoir un coût de 0€"

def test_annulation_avec_frais():
    """Test de l'annulation avec frais d'annulation."""
    chambre = Chambre(104, 120)
    reservation = Reservation(chambre, 5)
    frais = reservation.annuler(frais_annulation=100)
    assert frais == 100, "L'annulation doit coûter 100€"

def test_definir_prix_saison():
    """Test de la définition du prix de saison d'une chambre."""
    chambre = Chambre(105, 80)
    chambre.definir_prix_saison(1.5)  # Augmentation de 50%
    assert chambre.prix_saison == 120, "Le prix saisonnier devrait être 120€"
