import unittest
import json
import sqlite3
import os
from app import app
from database_manager import *


class TestBibliothequeIntegration(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    app.config['TESTING'] = True
    app.config['DATABASE'] = "bibliotheque_test.db"
    cls.app = app.test_client()

    with app.app_context():
      init_db()

  def setUp(self):
    with app.app_context():
      conn = get_db_connection()
      conn.execute("DELETE FROM livres")
      conn.commit()
      livres_default = [
          ('Les Misérables', 'Victor Hugo', False),
          ('Le Petit Prince', 'Antoine de Saint-Exupéry', False),
          ('1984', 'George Orwell', False),
        ]
      conn.executemany('INSERT INTO livres (titre, auteur, est_emprunte) VALUES (?, ?, ?)', livres_default)
      conn.commit()

  def test_ajouter_livre(self):
    response = self.app.post('/ajouter', data=json.dumps({'titre': 'Dune', 'auteur': 'Frank Herbert'}), content_type='application/json')
    self.assertEqual(response.status_code, 201)

    response = self.app.get('/livres')
    livres = json.loads(response.data)
    titres = [livre['titre'] for livre in livres]
    self.assertIn('Dune', titres)

  def test_emprunter_livre(self):
    response = self.app.post('/emprunter', data=json.dumps({'titre': 'Le Petit Prince'}), content_type='application/json')
    self.assertEqual(response.status_code, 200)

    response = self.app.get('/livres')
    livres = json.loads(response.data)
    petit_prince = next(livre for livre in livres if livre['titre'] == 'Le Petit Prince')
    self.assertTrue(petit_prince['est_emprunte'])

  def test_retourner_livre(self):
    self.app.post('/emprunter', data=json.dumps({'titre': '1984'}), content_type='application/json')

    response = self.app.post('/retourner', data=json.dumps({'titre': '1984'}), content_type='application/json')
    self.assertEqual(response.status_code, 200)

    response = self.app.get('/livres')
    livres = json.loads(response.data)
    livre_1984 = next(livre for livre in livres if livre['titre'] == '1984')
    self.assertFalse(livre_1984['est_emprunte'])

  def test_emprunter_livre_non_disponible(self):
    self.app.post('/emprunter', data=json.dumps({'titre': 'Les Misérables'}), content_type='application/json')

    response = self.app.post('/emprunter', data=json.dumps({'titre': 'Les Misérables'}), content_type='application/json')
    self.assertEqual(response.status_code, 404)

  def test_retourner_livre_non_emprunte(self):
    response = self.app.post('/retourner', data=json.dumps({'titre': 'Le Petit Prince'}), content_type='application/json')
    self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
  unittest.main()