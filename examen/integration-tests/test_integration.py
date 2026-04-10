"""
Tests d'intégration - Exercice 2
Eylon Soussan & Kiara

On teste les routes de l'API Flask avec une base de données SQLite en mémoire
pour ne pas toucher à la vraie base de données pendant les tests.
On utilise unittest et le client de test Flask.
"""

import unittest
import sys
import os
import sqlite3

# on ajoute le dossier courant au path pour pouvoir importer app.py et database_manager.py
sys.path.insert(0, os.path.dirname(__file__))

import database_manager
from app import app


# on utilise une base SQLite en mémoire partagée pour isoler les tests
def get_test_db_connection():
    conn = sqlite3.connect("file::memory:?cache=shared", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def init_test_db():
    # on recrée la table avant chaque test pour repartir de zéro
    with get_test_db_connection() as conn:
        conn.execute("DROP TABLE IF EXISTS livres")
        conn.execute('''CREATE TABLE livres
                     (id INTEGER PRIMARY KEY, titre TEXT, auteur TEXT, est_emprunte BOOLEAN)''')


class TestAPIBibliotheque(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # on remplace la connexion DB réelle par notre connexion de test (monkey-patching)
        database_manager.get_db_connection = get_test_db_connection
        app.config["TESTING"] = True
        cls.client = app.test_client()

    def setUp(self):
        # réinitialisation de la base avant chaque test
        init_test_db()

    # --- tests POST /ajouter ---

    def test_ajouter_livre_retourne_201(self):
        reponse = self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        self.assertEqual(reponse.status_code, 201)

    def test_ajouter_livre_message_confirmation(self):
        reponse = self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        self.assertIn("ajouté", reponse.get_json()["message"])

    def test_ajouter_plusieurs_livres(self):
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        reponse = self.client.post("/ajouter", json={"titre": "Le Petit Prince", "auteur": "Saint-Exupéry"})
        self.assertEqual(reponse.status_code, 201)

    # --- tests GET /livres ---

    def test_liste_vide_au_depart(self):
        reponse = self.client.get("/livres")
        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(reponse.get_json(), [])

    def test_liste_contient_livre_apres_ajout(self):
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        livres = self.client.get("/livres").get_json()
        self.assertEqual(len(livres), 1)
        self.assertEqual(livres[0]["titre"], "1984")

    def test_livre_a_champ_est_emprunte(self):
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        livres = self.client.get("/livres").get_json()
        self.assertIn("est_emprunte", livres[0])

    def test_nouveau_livre_est_disponible(self):
        # est_emprunte vaut 0 (False) pour un livre nouvellement ajouté
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        livres = self.client.get("/livres").get_json()
        self.assertEqual(livres[0]["est_emprunte"], 0)

    # --- tests POST /emprunter ---

    def test_emprunter_livre_disponible(self):
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        reponse = self.client.post("/emprunter", json={"titre": "1984"})
        self.assertEqual(reponse.status_code, 200)

    def test_emprunter_livre_message_succes(self):
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        reponse = self.client.post("/emprunter", json={"titre": "1984"})
        self.assertIn("emprunté", reponse.get_json()["message"])

    def test_emprunter_livre_inexistant_retourne_404(self):
        reponse = self.client.post("/emprunter", json={"titre": "Livre Inconnu"})
        self.assertEqual(reponse.status_code, 404)

    def test_emprunter_livre_deja_emprunte_retourne_404(self):
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        self.client.post("/emprunter", json={"titre": "1984"})
        reponse = self.client.post("/emprunter", json={"titre": "1984"})  # 2ème tentative
        self.assertEqual(reponse.status_code, 404)

    def test_emprunter_met_a_jour_est_emprunte_en_db(self):
        # après emprunt, la DB doit indiquer est_emprunte = 1
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        self.client.post("/emprunter", json={"titre": "1984"})
        livres = self.client.get("/livres").get_json()
        self.assertEqual(livres[0]["est_emprunte"], 1)

    # --- tests POST /retourner ---

    def test_retourner_livre_emprunte(self):
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        self.client.post("/emprunter", json={"titre": "1984"})
        reponse = self.client.post("/retourner", json={"titre": "1984"})
        self.assertEqual(reponse.status_code, 200)

    def test_retourner_livre_message_succes(self):
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        self.client.post("/emprunter", json={"titre": "1984"})
        reponse = self.client.post("/retourner", json={"titre": "1984"})
        self.assertIn("retourné", reponse.get_json()["message"])

    def test_retourner_livre_non_emprunte_retourne_404(self):
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        reponse = self.client.post("/retourner", json={"titre": "1984"})
        self.assertEqual(reponse.status_code, 404)

    def test_retourner_livre_inexistant_retourne_404(self):
        reponse = self.client.post("/retourner", json={"titre": "Livre Inconnu"})
        self.assertEqual(reponse.status_code, 404)

    def test_retourner_remet_livre_disponible_en_db(self):
        # après retour, est_emprunte doit repasser à 0 en base
        self.client.post("/ajouter", json={"titre": "1984", "auteur": "George Orwell"})
        self.client.post("/emprunter", json={"titre": "1984"})
        self.client.post("/retourner", json={"titre": "1984"})
        livres = self.client.get("/livres").get_json()
        self.assertEqual(livres[0]["est_emprunte"], 0)

    # --- scénario complet ---

    def test_scenario_complet(self):
        # on teste tout le cycle : ajout -> emprunt -> retour
        self.client.post("/ajouter", json={"titre": "Dune", "auteur": "Frank Herbert"})

        # livre bien ajouté et disponible
        livres = self.client.get("/livres").get_json()
        self.assertEqual(len(livres), 1)
        self.assertEqual(livres[0]["est_emprunte"], 0)

        # on emprunte
        rep = self.client.post("/emprunter", json={"titre": "Dune"})
        self.assertEqual(rep.status_code, 200)

        # livre marqué comme emprunté
        livres = self.client.get("/livres").get_json()
        self.assertEqual(livres[0]["est_emprunte"], 1)

        # on retourne
        rep = self.client.post("/retourner", json={"titre": "Dune"})
        self.assertEqual(rep.status_code, 200)

        # livre de nouveau disponible
        livres = self.client.get("/livres").get_json()
        self.assertEqual(livres[0]["est_emprunte"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
