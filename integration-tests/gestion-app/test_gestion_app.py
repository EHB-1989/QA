#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   test_gestion_app.py
@Time    :   2025/02/10 15:49:53
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   None
'''
import unittest
from app import app

class TestGestionApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_utilisateur(self):
        response = self.client.post("/utilisateurs", json={"nom": "Alice", "email": "alice@gmail.com"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Utilisateur créé avec succès"})

    def test_ajouter_tache(self):
        data = {
            "titre": "Range ta chambre",
            "description": "",
            "utilisateur_email": "alice@gmail.com"
        }
        response = self.client.post("/taches", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Tâche ajoutée avec succès"})

    def test_recuperer_taches(self):
        response = self.client.get("/taches/alice@gmail.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{"titre": "Range ta chambre", "description": ""}])



if __name__ == "__main__":
    print("Test gestion app")
    unittest.main()
    # Teardown
