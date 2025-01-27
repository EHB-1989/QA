import sqlite3
from poster import Poster


class DBManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS posts (title TEXT, content TEXT)"
        )
        self.connection.commit()

    def add_post(self, post):
        self.connection.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (post.title, post.content),
        )
        self.connection.commit()

    def get_posts(self):
        cursor = self.connection.execute("SELECT title, content FROM posts")
        return [Poster(title, content) for title, content in cursor]

    def __del__(self):
        self.connection.close()
