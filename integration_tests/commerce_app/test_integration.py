from integration_tests.commerce_app.produit import Produit
from integration_tests.commerce_app.panier import Panier


def test_ajout_produit_au_panier_succes():
    # On commence par la création des produits : 
    produit1 = Produit("Produit A", 20.0, 10)  
    produit2 = Produit("Produit B", 15.0, 5)   

    # Puis on fait la création du panier
    panier = Panier()

    # Après, on ajoute des produits au panier
    panier.ajouter_produit(produit1, 3)  
    panier.ajouter_produit(produit2, 2)  

    # On réalise les vérifications
    assert produit1.quantite_en_stock == 7, "Le stock du Produit A devrait être 7 après l'achat."
    assert produit2.quantite_en_stock == 3, "Le stock du Produit B devrait être 3 après l'achat."
    assert panier.calculer_total() == 75.0, "Le total du panier devrait être 75.0."


def test_ajout_produit_stock_insuffisant():
    # On commence par la création d'un produit avec un stock limité
    produit = Produit("Produit C", 10.0, 4)  

    # Puis on fait la création du panier
    panier = Panier()

    # On ajoute volontairement une quantité supérieure au stock
    panier.ajouter_produit(produit, 50)

    # Et on finit par faire les vérifications
    assert produit.quantite_en_stock == 4, "Normalement le stock ne devrait pas changer si la quantité demandée est insuffisante."
    assert panier.calculer_total() == 0.0, "Et normalement le total du panier devrait être 0 si aucun produit n'a été ajouté."


def test_calcul_prix_avec_remise():
    # On commence par la création d'un produit avec une remise
    produit = Produit("Produit D", 50.0, 5, pourcentage_remise=20)  

    # Puis, on construit le panier
    panier = Panier()

    # On ajoute le produit au panier
    panier.ajouter_produit(produit, 2)  

    # Et efin on réalise la vérifications
    assert produit.calculer_prix_apres_remise() == 40.0, "Le prix après remise devrait être 40.0."
    assert panier.calculer_total() == 80.0, "Et le total du panier devrait être 80.0 après application de la remise."


def test_combinaison_operations():
    # On commence par la création des produits
    produit1 = Produit("Produit E", 30.0, 5)   
    produit2 = Produit("Produit F", 25.0, 8)   
    produit3 = Produit("Produit G", 15.0, 0)   

    # Puis, on constuit le panier
    panier = Panier()

    # On ajoute les produits au panier
    panier.ajouter_produit(produit1, 2)  
    panier.ajouter_produit(produit2, 3)  
    panier.ajouter_produit(produit3, 1)  # échec attendu

    # Et on finit par les vérifications
    assert produit1.quantite_en_stock == 3, "Le stock du Produit E devrait être 3 après l'achat."
    assert produit2.quantite_en_stock == 5, "Le stock du Produit F devrait être 5 après l'achat."
    assert produit3.quantite_en_stock == 0, "Le stock du Produit G ne devrait pas changer car on avait initialisé notre stock à 0..."
    assert panier.calculer_total() == 135.0, "Enfin, le total du panier devrait être égale 135.0."


def test_panier_vide():
    # On commence par la création d'un panier vide
    panier = Panier()

    # Et on réalise une vérification du total
    assert panier.calculer_total() == 0.0, "Le total d'un panier vide devrait être 0.0."

