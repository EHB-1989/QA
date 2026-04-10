import sqlite3

DATABASE_NAME = "bibliotheque.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    livres_default = [
        ('Les Misérables', 'Victor Hugo', False),
        ('Le Petit Prince', 'Antoine de Saint-Exupéry', False),
        ('1984', 'George Orwell', False),
    ]
    conn = get_db_connection()
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS livres
                     (id INTEGER PRIMARY KEY, titre TEXT, auteur TEXT, est_emprunte BOOLEAN)''')
        # Vérifier si la table est vide avant d'ajouter les livres par défaut
        if conn.execute('SELECT * FROM livres').fetchone() is None:
            conn.executemany('INSERT INTO livres (titre, auteur, est_emprunte) VALUES (?, ?, ?)',
                             livres_default)
        conn.commit()
    finally:
        conn.close()

def get_livres_db():
    conn = get_db_connection()
    try:
        livres = conn.execute('SELECT * FROM livres').fetchall()
        return livres
    finally:
        conn.close()
        
def ajouter_livre_db(titre, auteur):
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO livres (titre, auteur, est_emprunte) VALUES (?, ?, ?)',
                     (titre, auteur, False))
        conn.commit()
    finally:
        conn.close()

def emprunter_livre_db(titre):
    conn = get_db_connection()
    try:
        livre = conn.execute('SELECT * FROM livres WHERE titre = ? AND est_emprunte = 0', (titre,)).fetchone()
        if livre:
            conn.execute('UPDATE livres SET est_emprunte = 1 WHERE titre = ?', (titre,))
            conn.commit()
            return True
        else:
            return False
    finally:
        conn.close()

def retourner_livre_db(titre):
    conn = get_db_connection()
    try:
        livre = conn.execute('SELECT * FROM livres WHERE titre = ? AND est_emprunte = 1', (titre,)).fetchone()
        if livre:
            conn.execute('UPDATE livres SET est_emprunte = 0 WHERE titre = ?', (titre,))
            conn.commit()
            return True
        else:
            return False
    finally:
        conn.close()