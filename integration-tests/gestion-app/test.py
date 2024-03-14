import unittest
import sqlite3
from tache import *
from utilisateur import *

def test_ajout_et_recuperation_utilisateur_tache(self) :
    utilisateur = Utilisateur("test@gmail.com","Testeur")
    self. gestionnaire. ajouter_utilisateur(utilisateur)

    tache = Tache("Tache Test", "Description de la tache test", "test@gmail.com")
    self. gestionnaire. ajouter_tache (tache)

    taches_recuperees = self. gestionnaire.recuperer_taches ( "test@gmail.com" )
    self.assertEqua1(len(taches_recuperees), 1)
    self.assertEqua1(taches_recuperees[0]["titre"], "Tache Test")
    self.assertEqua1(taches_recuperees[0]["description"], "Description de la tache test")