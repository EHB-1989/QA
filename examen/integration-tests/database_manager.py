import sqlite3

DATABASE_NAME = "bibliotheque.db"

# Retourne une connexion à la base de données.
def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# Initialise la base de données avec une table 'livres' et ajoute des livres par défaut.
def init_db():
    livres_default = [
        ('Les Misérables', 'Victor Hugo', False),
        ('Le Petit Prince', 'Antoine de Saint-Exupéry', False),
        ('1984', 'George Orwell', False),
    ]
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS livres
                     (id INTEGER PRIMARY KEY, titre TEXT, auteur TEXT, est_emprunte BOOLEAN)''')
        if conn.execute('SELECT * FROM livres').fetchone() is None:
            conn.executemany('INSERT INTO livres (titre, auteur, est_emprunte) VALUES (?, ?, ?)',
                             livres_default)

# Récupère tous les livres de la base de données.
def get_livres_db():
    with get_db_connection() as conn:
       livres = conn.execute('SELECT * FROM livres').fetchall()
       return livres
        
# Ajoute un nouveau livre à la base de données.
def ajouter_livre_db(titre, auteur):
    with get_db_connection() as conn:
        conn.execute('INSERT INTO livres (titre, auteur, est_emprunte) VALUES (?, ?, ?)',
                     (titre, auteur, False))

# Marque un livre comme emprunté dans la base de données si disponible.
def emprunter_livre_db(titre):
    with get_db_connection() as conn:
        livre = conn.execute('SELECT * FROM livres WHERE titre = ? AND est_emprunte = 0', (titre,)).fetchone()
        if livre:
            conn.execute('UPDATE livres SET est_emprunte = 1 WHERE titre = ?', (titre,))
            return True
        else:
            return False

# Marque un livre comme retourné dans la base de données s'il était emprunté.
def retourner_livre_db(titre):
    with get_db_connection() as conn:
        livre = conn.execute('SELECT * FROM livres WHERE titre = ? AND est_emprunte = 1', (titre,)).fetchone()
        if livre:
            conn.execute('UPDATE livres SET est_emprunte = 0 WHERE titre = ?', (titre,))
            return True
        else:
            return False
