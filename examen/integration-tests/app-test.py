import unittest
import json
from app import app
from database_manager import get_db_connection

class TestIntegrationBibliotheque(unittest.TestCase):
  def setUp(self):
    self.client = app.test_client()
    self.db_test = "test_bibliotheque.db"

  def test_ajout_livre(self):
    response = self.client.post('/ajouter',
      json={
        'titre': 'Notre-Dame de Paris',
        'auteur': 'Victor Hugo'
      })
    self.assertEqual(response.json['message'], 'Livre ajouté avec succès')
    self.assertEqual(response.status_code, 201)

    with get_db_connection() as conn:
      livre = conn.execute('SELECT * FROM livres WHERE titre = ?',
                          ('Notre-Dame de Paris',)).fetchone()
      self.assertIsNotNone(livre)
      self.assertEqual(livre['titre'], 'Notre-Dame de Paris')

  def test_liste_livres(self):
    response = self.client.get('/livres')
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertIsInstance(data, list)
    self.assertTrue(len(data) > 0)

  def test_emprunt_livre(self):
    self.client.post('/ajouter',
      json={
        'titre': "Tous les hommes n'habitent pas le monde de la même façon",
        'auteur': 'Jean-Paul Dubois'
      })

    response = self.client.post('/emprunter',
      json={'titre': "Tous les hommes n'habitent pas le monde de la même façon"})
    self.assertEqual(response.json['message'], 'Livre emprunté avec succès')
    self.assertEqual(response.status_code, 200)

    with get_db_connection() as conn:
      livre = conn.execute('SELECT est_emprunte FROM livres WHERE titre = ?',
                          ("Tous les hommes n'habitent pas le monde de la même façon",)).fetchone()
      self.assertTrue(livre['est_emprunte'])

    # Un double emprunt doit être impossible.
    response = self.client.post('/emprunter',
      json={'titre': 'Harry Potter'})
    self.assertEqual(response.json['message'], 'Livre non disponible')
    self.assertEqual(response.status_code, 404)

  def test_retour_livre(self):
    response = self.client.post('/retourner',
      json={'titre': "Tous les hommes n'habitent pas le monde de la même façon"})
    self.assertEqual(response.json['message'], 'Livre retourné avec succès')
    self.assertEqual(response.status_code, 200)

    with get_db_connection() as conn:
      livre = conn.execute('SELECT est_emprunte FROM livres WHERE titre = ?',
                          ("Tous les hommes n'habitent pas le monde de la même façon",)).fetchone()
      self.assertFalse(livre['est_emprunte'])

    # Un double retour doit être impossible.
    response = self.client.post('/retourner',
      json={'titre': "Tous les hommes n'habitent pas le monde de la même façon"})
    self.assertEqual(response.json['message'], 'Livre non trouvé ou déjà retourné')
    self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()