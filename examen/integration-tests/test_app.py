import os
import tempfile
import unittest
import database_manager
from app import app

class TestBibliothequeAPI(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp(suffix=".db")
        os.close(self.db_fd)

        database_manager.DATABASE_NAME = self.db_path
        app.config["TESTING"] = True
        self.client = app.test_client()

        database_manager.init_db()

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.unlink(self.db_path)

    def test_lister_livres_retourne_les_livres_par_defaut(self):
        response = self.client.get("/livres")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(len(data), 3)

        titres = [livre["titre"] for livre in data]
        self.assertIn("Les Misérables", titres)
        self.assertIn("Le Petit Prince", titres)
        self.assertIn("1984", titres)

    def test_ajouter_livre(self):
        response = self.client.post(
            "/ajouter",
            json={"titre": "Dune", "auteur": "Frank Herbert"},
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["message"], "Livre ajouté avec succès")

        response = self.client.get("/livres")
        data = response.get_json()
        titres = [livre["titre"] for livre in data]
        self.assertIn("Dune", titres)

    def test_emprunter_livre_disponible(self):
        response = self.client.post("/emprunter", json={"titre": "1984"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Livre emprunté avec succès")

        response = self.client.get("/livres")
        data = response.get_json()
        livre = next(livre for livre in data if livre["titre"] == "1984")
        self.assertEqual(livre["est_emprunte"], 1)

    def test_emprunter_livre_non_disponible(self):
        self.client.post("/emprunter", json={"titre": "1984"})
        response = self.client.post("/emprunter", json={"titre": "1984"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()["message"], "Livre non disponible")

    def test_retourner_livre_emprunte(self):
        self.client.post("/emprunter", json={"titre": "1984"})
        response = self.client.post("/retourner", json={"titre": "1984"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Livre retourné avec succès")

        response = self.client.get("/livres")
        data = response.get_json()
        livre = next(livre for livre in data if livre["titre"] == "1984")
        self.assertEqual(livre["est_emprunte"], 0)

    def test_retourner_livre_non_emprunte(self):
        response = self.client.post("/retourner", json={"titre": "1984"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.get_json()["message"],
            "Livre non trouvé ou déjà retourné",
        )

    def test_emprunter_livre_inexistant(self):
        response = self.client.post("/emprunter", json={"titre": "Livre inconnu"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()["message"], "Livre non disponible")


if __name__ == "__main__":
    unittest.main()