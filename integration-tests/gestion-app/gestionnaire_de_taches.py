import sqlite3


class GestionnaireDeTaches:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS utilisateurs (email TEXT PRIMARY KEY, nom TEXT)"
        )
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS taches (titre TEXT, description TEXT, utilisateur_email TEXT, FOREIGN KEY(utilisateur_email) REFERENCES utilisateurs(email))"
        )
        self.conn.commit()

    def ajouter_utilisateur(self, utilisateur):
        self.conn.execute(
            "INSERT INTO utilisateurs (email, nom) VALUES (?, ?)",
            (utilisateur.email, utilisateur.nom),
        )
        self.conn.commit()

    def ajouter_tache(self, tache):
        self.conn.execute(
            "INSERT INTO taches (titre, description, utilisateur_email) VALUES (?, ?, ?)",
            (tache.titre, tache.description, tache.utilisateur_email),
        )
        self.conn.commit()

    def recuperer_taches(self, utilisateur_email):
        cursor = self.conn.execute(
            "SELECT titre, description FROM taches WHERE utilisateur_email = ?",
            (utilisateur_email,),
        )
        return [{"titre": row[0], "description": row[1]} for row in cursor]

    def __del__(self):
        self.conn.close()
