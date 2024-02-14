from produit import Produit
from panier import Panier


produit1 = Produit("sac", 10.00, 5)
produit2 = Produit("Stylo", 2.00, 10, 10)

panier = Panier()

panier.ajouter_produit(produit1, 3)
panier.ajouter_produit(produit2, 5)

assert panier.produits == {produit1: 3, produit2: 5}

total_prevu = (
    produit1.calculer_prix_apres_remise() * 3
    + produit2.calculer_prix_apres_remise() * 5
)

assert panier.calculer_total() == total_prevu

assert produit1.quantite_en_stock == 2

assert produit1.acheter(1) is True


