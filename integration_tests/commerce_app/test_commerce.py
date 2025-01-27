from integration_tests.commerce_app.panier import Panier
from integration_tests.commerce_app.produit import Produit
import pytest

def test_add_produit_to_panier_should_work():
    # Arrange
    panier = Panier()
    produit = Produit("T-shirt", 20, 10)
    # Act
    panier.ajouter_produit(produit, 1)
    # Assert
    assert produit in panier.produits
    assert panier.produits[produit] == 1
    assert produit.quantite_en_stock == 9

def test_buy_produit_from_panier_should_not_work():
    # Arrange
    panier = Panier()
    produit = Produit("T-shirt", 20, 0)
    # Act
    panier.ajouter_produit(produit, 1)
    # Assert
    assert produit not in panier.produits
    assert produit.quantite_en_stock == 0

def test_buy_produit_should_have_error():
    # Arrange
    panier = Panier()
    produit = Produit("T-shirt", 20, "test")
    # Act and Assert
    with pytest.raises(TypeError):
        panier.ajouter_produit(produit, "test")

def test_calculer_total_should_work():
    # Arrange
    panier = Panier()
    produit1 = Produit("T-shirt", 20, 10, 10)
    produit2 = Produit("Pantalon", 50, 5, 20)
    # Act
    panier.ajouter_produit(produit1, 1)
    panier.ajouter_produit(produit2, 2)
    # Assert
    assert panier.calculer_total() == 98.0

def test_calculer_total_should_not_work():
    # Arrange
    panier = Panier()
    produit = Produit("T-shirt", -20, 10, 10)
    # Act
    panier.ajouter_produit(produit, 1)
    # Assert
    assert panier.calculer_total() == 0.0, "Should return 0.0 because the price is negative"

def test_calculer_total_with_no_produit_should_return_zero():
    # Arrange
    panier = Panier()
    # Act
    total = panier.calculer_total()
    # Assert
    assert total == 0

def test_produit_quantity_should_be_zero():
    # Arrange
    produit = Produit("T-shirt", 20, 10)
    # Act
    produit.acheter(10)
    produit.acheter(1)
    # Assert
    assert produit.quantite_en_stock == 0