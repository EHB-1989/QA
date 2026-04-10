import tempfile
import unittest

import database_manager
from app import app as flask_app


class TestBibliothequeIntegration(unittest.TestCase):
    def setUp(self):
        # Chaque test utilise sa propre base SQLite pour rester indépendant.
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_database_name = database_manager.DATABASE_NAME
        database_manager.DATABASE_NAME = f"{self.temp_dir.name}/test_bibliotheque.db"

        flask_app.config["TESTING"] = True
        database_manager.init_db()
        self.client = flask_app.test_client()

    def tearDown(self):
        database_manager.DATABASE_NAME = self.original_database_name
        self.temp_dir.cleanup()

    def _get_livre(self, titre):
        # Ce helper permet de vérifier l'état réellement persisté en base.
        with database_manager.get_db_connection() as conn:
            return conn.execute(
                "SELECT titre, auteur, est_emprunte FROM livres WHERE titre = ?",
                (titre,),
            ).fetchone()

    def test_lister_livres_retourne_les_livres_initiaux(self):
        response = self.client.get("/livres")

        self.assertEqual(response.status_code, 200)

        livres = response.get_json()
        titres = [livre["titre"] for livre in livres]

        self.assertEqual(len(livres), 3)
        self.assertIn("Les Misérables", titres)
        self.assertIn("Le Petit Prince", titres)
        self.assertIn("1984", titres)

    def test_ajouter_livre_persiste_le_nouveau_livre(self):
        response = self.client.post(
            "/ajouter",
            json={"titre": "Dune", "auteur": "Frank Herbert"},
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {"message": "Livre ajouté avec succès"})

        livre = self._get_livre("Dune")
        self.assertIsNotNone(livre)
        self.assertEqual(livre["auteur"], "Frank Herbert")
        self.assertEqual(livre["est_emprunte"], 0)

    def test_emprunter_livre_disponible_met_a_jour_son_etat(self):
        response = self.client.post("/emprunter", json={"titre": "1984"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Livre emprunté avec succès"})

        livre = self._get_livre("1984")
        self.assertIsNotNone(livre)
        self.assertEqual(livre["est_emprunte"], 1)

    def test_emprunter_livre_indisponible_retourne_404(self):
        self.client.post("/emprunter", json={"titre": "1984"})

        response = self.client.post("/emprunter", json={"titre": "1984"})

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {"message": "Livre non disponible"})

    def test_retourner_livre_emprunte_le_rend_disponible(self):
        self.client.post("/emprunter", json={"titre": "Le Petit Prince"})

        response = self.client.post("/retourner", json={"titre": "Le Petit Prince"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Livre retourné avec succès"})

        livre = self._get_livre("Le Petit Prince")
        self.assertIsNotNone(livre)
        self.assertEqual(livre["est_emprunte"], 0)

    def test_retourner_livre_non_emprunte_retourne_404(self):
        response = self.client.post("/retourner", json={"titre": "Les Misérables"})

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.get_json(),
            {"message": "Livre non trouvé ou déjà retourné"},
        )


if __name__ == "__main__":
    unittest.main()
