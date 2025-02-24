import pytest
from app import Livre, Bibliotheque

def test_livre_emprunter():
    livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    assert livre.emprunter() == True
    assert livre.emprunter() == False

def test_livre_retourner():
    livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    livre.emprunter()
    assert livre.retourner() == True
    assert livre.retourner() == False

def test_bibliotheque_ajouter_livre():
    biblio = Bibliotheque()
    livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    biblio.ajouter_livre(livre)
    assert len(biblio.livres) == 1

def test_bibliotheque_emprunter_livre():
    biblio = Bibliotheque()
    livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    biblio.ajouter_livre(livre)
    assert biblio.emprunter_livre("Le Petit Prince") == True
    assert biblio.emprunter_livre("Le Petit Prince") == False

def test_bibliotheque_retourner_livre():
    biblio = Bibliotheque()
    livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    biblio.ajouter_livre(livre)
    biblio.emprunter_livre("Le Petit Prince")
    assert biblio.retourner_livre("Le Petit Prince") == True
    assert biblio.retourner_livre("Le Petit Prince") == False