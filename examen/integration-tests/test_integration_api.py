"""
Tests d'intégration : client HTTP Flask + SQLite réel (fichier temporaire).

Chaque test repart d'une base réinitialisée (mêmes livres par défaut que init_db).
"""
import os
import tempfile
import unittest


class TestBibliothequeIntegrationAPI(unittest.TestCase):
    """Vérifie les routes et la cohérence avec la persistance SQLite."""

    @classmethod
    def setUpClass(cls):
        # Base dédiée aux tests : n'écrase pas bibliotheque.db du développeur.
        fd, cls._db_path = tempfile.mkstemp(suffix=".db")
        os.close(fd)
        os.environ["BIBLIOTHEQUE_DB"] = cls._db_path

        # Import après BIBLIOTHEQUE_DB : get_db_connection() pointe sur le fichier temporaire.
        from app import app as flask_app
        import database_manager as dm

        cls._dm = dm
        cls.app = flask_app
        cls.app.config["TESTING"] = True
        cls.client = cls.app.test_client()
        dm.init_db()

    @classmethod
    def tearDownClass(cls):
        if "BIBLIOTHEQUE_DB" in os.environ:
            del os.environ["BIBLIOTHEQUE_DB"]
        try:
            os.unlink(cls._db_path)
        except OSError:
            pass

    def setUp(self):
        # Isolation : table vidée puis réinjection des 3 livres par défaut.
        with self._dm.get_db_connection() as conn:
            conn.execute("DELETE FROM livres")
        self._dm.init_db()

    def test_get_livres_200_et_trois_livres_par_defaut(self):
        r = self.client.get("/livres")
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(len(data), 3)
        titres = {row["titre"] for row in data}
        self.assertIn("1984", titres)
        self.assertIn("Le Petit Prince", titres)

    def test_post_ajouter_201_et_livre_visible_en_get(self):
        r = self.client.post(
            "/ajouter",
            json={"titre": "Dune", "auteur": "Frank Herbert"},
        )
        self.assertEqual(r.status_code, 201)
        self.assertIn("succès", r.get_json().get("message", ""))

        listed = self.client.get("/livres").get_json()
        titres = {row["titre"] for row in listed}
        self.assertIn("Dune", titres)
        dune = next(row for row in listed if row["titre"] == "Dune")
        self.assertEqual(dune["auteur"], "Frank Herbert")
        self.assertEqual(dune["est_emprunte"], 0)

    def test_post_emprunter_200_met_a_jour_la_base(self):
        r = self.client.post("/emprunter", json={"titre": "1984"})
        self.assertEqual(r.status_code, 200)
        row = next(
            x for x in self.client.get("/livres").get_json() if x["titre"] == "1984"
        )
        self.assertEqual(row["est_emprunte"], 1)

    def test_post_emprunter_404_si_deja_emprunte(self):
        self.client.post("/emprunter", json={"titre": "1984"})
        r = self.client.post("/emprunter", json={"titre": "1984"})
        self.assertEqual(r.status_code, 404)

    def test_post_emprunter_404_si_titre_inconnu(self):
        r = self.client.post("/emprunter", json={"titre": "Inconnu"})
        self.assertEqual(r.status_code, 404)

    def test_post_retourner_200_apres_emprunt(self):
        self.client.post("/emprunter", json={"titre": "1984"})
        r = self.client.post("/retourner", json={"titre": "1984"})
        self.assertEqual(r.status_code, 200)
        row = next(
            x for x in self.client.get("/livres").get_json() if x["titre"] == "1984"
        )
        self.assertEqual(row["est_emprunte"], 0)

    def test_post_retourner_404_si_pas_emprunte(self):
        r = self.client.post("/retourner", json={"titre": "1984"})
        self.assertEqual(r.status_code, 404)

    def test_scenario_complet_ajouter_emprunter_retourner(self):
        # Enchaînement réaliste : ajout → emprunt → retour, états vérifiés via GET.
        self.client.post("/ajouter", json={"titre": "Hamlet", "auteur": "Shakespeare"})
        self.assertEqual(
            self.client.post("/emprunter", json={"titre": "Hamlet"}).status_code, 200
        )
        self.assertEqual(
            self.client.post("/emprunter", json={"titre": "Hamlet"}).status_code, 404
        )
        self.assertEqual(
            self.client.post("/retourner", json={"titre": "Hamlet"}).status_code, 200
        )
        hamlet = next(
            x
            for x in self.client.get("/livres").get_json()
            if x["titre"] == "Hamlet"
        )
        self.assertEqual(hamlet["est_emprunte"], 0)


if __name__ == "__main__":
    unittest.main()