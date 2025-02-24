#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File    :   test_app.py
@Time    :   2025/02/24
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   None
"""

import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_ajouter_livre(self):
        response = self.client.post(
            "/ajouter", json={"titre": "Livre 1", "auteur": "Auteur 1"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Livre ajouté avec succès"})

    def test_lister_livres(self):
        response = self.client.get("/livres")
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json, [])
        expected_books = [
            {
                "id": 1,
                "titre": "Les Misérables",
                "auteur": "Victor Hugo",
                "est_emprunte": False,
            },
            {
                "id": 2,
                "titre": "Le Petit Prince",
                "auteur": "Antoine de Saint-Exupéry",
                "est_emprunte": False,
            },
            {
                "id": 3,
                "titre": "1984",
                "auteur": "George Orwell",
                "est_emprunte": False,
            },
        ]

        actual_books = response.json
        filtered_actual_books = [
            book for book in actual_books if book in expected_books
        ]
        self.assertEqual(filtered_actual_books, expected_books)

    def test_emprunter(self):
        response = self.client.post("/emprunter", json={"titre": "Bob"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Livre non disponible"})

        response = self.client.post("/emprunter", json={"titre": "Livre 1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Livre emprunté avec succès"})

    def test_retourner_livre(self):
        response = self.client.post("/retourner", json={"titre": "Livre 1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Livre retourné avec succès"})
        # Retournons le une seconde fois pour essayer
        response = self.client.post("/retourner", json={"titre": "Livre 1"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json, {"message": "Livre non trouvé ou déjà retourné"}
        )
        # Retournons un livre qui n'existe pas
        response = self.client.post("/retourner", json={"titre": "Jen'existe pas"})
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
