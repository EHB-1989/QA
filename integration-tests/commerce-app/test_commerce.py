from panier import Panier
from produit import Produit
import pytest

def test_acheter_produit():
    produit = Produit("Livre", 10, 100)
    assert produit.acheter(200) == False
    assert produit.acheter(-50) == False
    assert produit.acheter(100) == True
    
def test_prix_produit():
    produit = Produit("Livre", 10, 100, 10)
    assert produit.calculer_prix_apres_remise() == 9
    produit.pourcentage_remise = 60
    assert produit.calculer_prix_apres_remise() == 4
    produit.pourcentage_remise = 0
    assert produit.calculer_prix_apres_remise() == 10
    
def test_panier_ajouterProduit():
    panier=Panier()
    produit = Produit("Livre", 10, 100)
    
    assert panier.calculer_total() == 0
    
    panier.ajouter_produit(produit, 10)
    assert panier.calculer_total() == 100
    assert produit.quantite_en_stock == 90
    
    panier.ajouter_produit(produit, 100)
    assert panier.calculer_total() == 100
    assert produit.quantite_en_stock == 90
    
    panier.ajouter_produit(produit, -50)
    assert panier.calculer_total() == 100