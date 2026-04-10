# Examen Tests

> Auteurs :\
> Adrien LE NINIVEN\
> Peter JARQUIS

Ce dépôt regroupe les travaux d’examen autour des tests logiciels : tests unitaires, performance et intégration sur des mini-applications Python.

## Exercice 1 — Tests unitaires (unittest)

**Dossier :** `unit-tests/`

Application minimale de gestion de bibliothèque : classes `Livre` (titre, auteur, état emprunté) et `Bibliotheque` (inventaire, emprunt et retour par titre). Les tests dans `test_bibliotheque.py` couvrent les cas nominaux et les refus (livre déjà emprunté, titre inconnu, etc.).

**Lancer les tests :**

```bash
cd unit-tests && python3 -m unittest discover -v
```

Exercice 2 — Tests d’intégration (API Flask + SQLite)
Dossier : integration-tests/

Même métier (livres, emprunt, retour) exposé via une API HTTP Flask et une base SQLite (database_manager.py). Les tests d’intégration utilisent le client de test Flask et un fichier SQLite temporaire (BIBLIOTHEQUE_DB) pour ne pas écraser bibliotheque.db local et pour isoler chaque scénario.

Prérequis : flask (ex. pip install flask).

Lancer les tests :

cd examen/integration-tests && python3 -m unittest discover -v


Fichiers : app.py (routes), database_manager.py (persistance), test_integration_api.py (scénarios GET/POST et enchaînements).


## Exercice 3 — Tests d’intégration
