import unittest
import json
import os
import sys

# On ajoute le dossier courant au chemin pour pouvoir importer app.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import database_manager
from app import app
from database_manager import init_db


class TestIntegrationBibliotheque(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Création du client Flask une seule fois."""
        app.config["TESTING"] = True
        cls.client = app.test_client()

    def setUp(self):
        """Avant chaque test : on utilise une base SQLite dédiée."""
        self.test_db = f"test_bibliotheque_{self._testMethodName}.db"
        database_manager.DATABASE_NAME = self.test_db

        if os.path.exists(self.test_db):
            try:
                os.remove(self.test_db)
            except PermissionError:
                pass

        init_db()

    def tearDown(self):
        """Après chaque test : suppression de la base du test."""
        if os.path.exists(self.test_db):
            try:
                os.remove(self.test_db)
            except PermissionError:
                pass

    def post(self, url, payload):
        return self.client.post(
            url,
            data=json.dumps(payload),
            content_type="application/json"
        )

    # --------------------------------------------------------
    # GET /livres
    # --------------------------------------------------------

    def test_lister_livres(self):
        """La liste des livres doit retourner 200 et contenir les livres par défaut."""
        response = self.client.get("/livres")
        self.assertEqual(response.status_code, 200)

        livres = json.loads(response.data)
        titres = [l["titre"] for l in livres]

        self.assertIn("1984", titres)
        self.assertIn("Le Petit Prince", titres)

    # --------------------------------------------------------
    # POST /ajouter
    # --------------------------------------------------------

    def test_ajouter_livre(self):
        """Ajouter un livre doit retourner 201 et le livre doit apparaître dans la liste."""
        response = self.post("/ajouter", {"titre": "Dune", "auteur": "Frank Herbert"})
        self.assertEqual(response.status_code, 201)

        livres = json.loads(self.client.get("/livres").data)
        titres = [l["titre"] for l in livres]

        self.assertIn("Dune", titres)

    def test_ajouter_livre_message_reponse(self):
        """Ajouter un livre doit retourner un message de succès."""
        response = self.post("/ajouter", {"titre": "Dracula", "auteur": "Bram Stoker"})
        self.assertEqual(response.status_code, 201)

        data = json.loads(response.data)
        self.assertIn("message", data)
        self.assertEqual(data["message"], "Livre ajouté avec succès")

    # --------------------------------------------------------
    # POST /emprunter
    # --------------------------------------------------------

    def test_emprunter_livre_disponible(self):
        """Emprunter un livre disponible doit retourner 200."""
        response = self.post("/emprunter", {"titre": "1984"})
        self.assertEqual(response.status_code, 200)

    def test_emprunter_livre_deja_emprunte(self):
        """Emprunter un livre déjà emprunté doit retourner 404."""
        self.post("/emprunter", {"titre": "1984"})
        response = self.post("/emprunter", {"titre": "1984"})
        self.assertEqual(response.status_code, 404)

    def test_emprunter_livre_change_etat(self):
        """Après emprunt, le livre doit apparaître comme emprunté dans la liste."""
        self.post("/emprunter", {"titre": "1984"})

        livres = json.loads(self.client.get("/livres").data)
        livre = next(l for l in livres if l["titre"] == "1984")

        self.assertTrue(livre["est_emprunte"])

    def test_emprunter_livre_inexistant(self):
        """Emprunter un livre inexistant doit retourner 404."""
        response = self.post("/emprunter", {"titre": "Livre Fantome"})
        self.assertEqual(response.status_code, 404)

    # --------------------------------------------------------
    # POST /retourner
    # --------------------------------------------------------

    def test_retourner_livre_emprunte(self):
        """Retourner un livre emprunté doit retourner 200."""
        self.post("/emprunter", {"titre": "Le Petit Prince"})
        response = self.post("/retourner", {"titre": "Le Petit Prince"})
        self.assertEqual(response.status_code, 200)

    def test_retourner_livre_non_emprunte(self):
        """Retourner un livre qui n'est pas emprunté doit retourner 404."""
        response = self.post("/retourner", {"titre": "Les Misérables"})
        self.assertEqual(response.status_code, 404)

    def test_retourner_livre_change_etat(self):
        """Après retour, le livre doit redevenir disponible."""
        self.post("/emprunter", {"titre": "1984"})
        self.post("/retourner", {"titre": "1984"})

        livres = json.loads(self.client.get("/livres").data)
        livre = next(l for l in livres if l["titre"] == "1984")

        self.assertFalse(livre["est_emprunte"])

    def test_retourner_livre_inexistant(self):
        """Retourner un livre inexistant doit retourner 404."""
        response = self.post("/retourner", {"titre": "Livre Fantome"})
        self.assertEqual(response.status_code, 404)

    # --------------------------------------------------------
    # Scénario complet
    # --------------------------------------------------------

    def test_flux_complet(self):
        """
        Scénario bout-en-bout :
        ajouter un livre -> l'emprunter -> le retourner -> vérifier qu'il est disponible.
        """
        self.post("/ajouter", {"titre": "Fondation", "auteur": "Isaac Asimov"})

        r = self.post("/emprunter", {"titre": "Fondation"})
        self.assertEqual(r.status_code, 200)

        r = self.post("/retourner", {"titre": "Fondation"})
        self.assertEqual(r.status_code, 200)

        livres = json.loads(self.client.get("/livres").data)
        fondation = next(l for l in livres if l["titre"] == "Fondation")
        self.assertFalse(fondation["est_emprunte"])


if __name__ == "__main__":
    unittest.main(verbosity=2)