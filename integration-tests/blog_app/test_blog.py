import sqlite3

# Simuler la classe Poster si elle n'existe pas
class Poster:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"Poster(title='{self.title}', content='{self.content}')"

# Importer la classe DBManager (déjà fournie)
class DBManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, content TEXT)')
        self.connection.commit()

    def add_post(self, post):
        self.connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (post.title, post.content))
        self.connection.commit()

    def get_posts(self):
        cursor = self.connection.execute('SELECT title, content FROM posts')
        return [Poster(title, content) for title, content in cursor]

    def __del__(self):
        self.connection.close()

# Test unitaire
def test_db_manager():
    db = DBManager(":memory:")  # Base en mémoire pour éviter de créer un fichier

    # Ajouter un post
    post = Poster("Test Title", "This is a test content")
    db.add_post(post)

    # Récupérer les posts
    posts = db.get_posts()

    # Vérifier que le post est bien ajouté
    assert len(posts) == 1, "Le nombre de posts devrait être 1"
    assert posts[0].title == "Test Title", "Le titre ne correspond pas"
    assert posts[0].content == "This is a test content", "Le contenu ne correspond pas"

    print("✅ Test réussi : les posts sont bien insérés et récupérés !")

# Lancer le test
test_db_manager()
