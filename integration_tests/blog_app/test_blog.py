from integration_tests.blog_app.poster import Poster
from integration_tests.blog_app.database_manager import DBManager
import pytest
import os

@pytest.fixture
def db_manager():
    db_name = "test.db"
    db_manager = DBManager(db_name)
    yield db_manager
    del db_manager

    # to clear database after running tests
    if os.path.exists(db_name):
        os.remove(db_name)


def test_add_post_should_work(db_manager):
    # Arrange
    post = Poster("title", "content")
    # Act
    db_manager.add_post(post)
    # Assert
    posts = db_manager.get_posts()
    assert len(posts) == 1
    assert posts[0].title == "title"
    assert posts[0].content == "content"

def test_add_post_should_fail(db_manager):
    # Arrange
    # Act and Assert
    with pytest.raises(AttributeError):
        db_manager.add_post("title")

def test_get_posts_should_work(db_manager):
    # Arrange
    post1 = Poster("title1", "content1")
    post2 = Poster("title2", "content2")
    db_manager.add_post(post1)
    db_manager.add_post(post2)
    # Act
    posts = db_manager.get_posts()
    # Assert
    assert len(posts) == 2
    assert posts[0].title == "title1"
    assert posts[0].content == "content1"
    assert posts[1].title == "title2"
    assert posts[1].content == "content2"

