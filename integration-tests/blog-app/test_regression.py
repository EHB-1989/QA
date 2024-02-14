from database_manager import DBManager
from poster import Poster

def test_add_post_and_get_posts():
    db_manager = DBManager(":memory:")

    post = Poster("Mon post", "Ceci est le contenu de mon post.")

    db_manager.add_post(post)

    posts = db_manager.get_posts()

    assert len(posts) == 1
    assert posts[0].title == post.title
    assert posts[0].content == post.content

    del db_manager
