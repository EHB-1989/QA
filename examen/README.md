# Examen Tests

> Auteurs :\
> Adrien LE NINIVEN\
> Peter JARQUIS

Ce dépôt regroupe les travaux d’examen autour des tests logiciels : tests unitaires, intégration (API + base), parcours **e2e** sur le site public [python.org](https://www.python.org/) (Selenium).

## Exercice 1 — Tests unitaires (unittest)

**Dossier :** `unit-tests/`

Application minimale de gestion de bibliothèque : classes `Livre` (titre, auteur, état emprunté) et `Bibliotheque` (inventaire, emprunt et retour par titre). Les tests dans `test_bibliotheque.py` couvrent les cas nominaux et les refus (livre déjà emprunté, titre inconnu, etc.).

**Lancer les tests :**

```bash
cd examen/unit-tests && python3 -m unittest discover -v
```

## Exercice 2 — Tests d’intégration (API Flask + SQLite)
Dossier : integration-tests/

Même métier (livres, emprunt, retour) exposé via une API HTTP Flask et une base SQLite (database_manager.py). Les tests d’intégration utilisent le client de test Flask et un fichier SQLite temporaire (BIBLIOTHEQUE_DB) pour ne pas écraser bibliotheque.db local et pour isoler chaque scénario.

Prérequis : flask (ex. pip install flask).

**Lancer les tests :**

```bash
cd examen/integration-tests && python3 -m unittest discover -v
```


## Exercice 3 — Tests de bout en bout (Selenium + unittest)

**Dossier :** `e2e-tests/`

Parcours automatisé sur **www.python.org** : page d’accueil → menu **Documentation** (`/doc/`) → lien **Beginner’s Guide** vers le wiki → vérification du titre et de l’URL de la page ouverte. Le fichier `test_python_org_documentation.py` utilise **unittest** (`setUp` / `tearDown`), **WebDriverWait** et des sélecteurs ciblant le menu puis le widget « Beginner » sur la page documentation (éviter les liens du méga-menu non interactifs sans survol).

**Prérequis :** `selenium` (ex. `pip install selenium`), **Mozilla Firefox** et **geckodriver** installé et accessible dans le `PATH` (versions compatibles entre elles).

**Lancer les tests :**

```bash
cd examen/e2e-tests && python3 -m unittest discover -v
```

**Fichier :** `test_python_org_documentation.py`.
