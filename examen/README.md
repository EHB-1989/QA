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

## Exercice 2 — Tests de performance

## Exercice 3 — Tests d’intégration
