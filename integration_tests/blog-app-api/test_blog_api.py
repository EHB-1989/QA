import pytest
import app as App


# TODO: add mocking on db_manager
@pytest.fixture
def db_manager():
    db_name = "test.db"
    db_manager = DBManager(db_name)
    yield db_manager
    del db_manager

    # to clear database after running tests
    if os.path.exists(db_name):
        os.remove(db_name)


@pytest.fixture()
def server():
    app = App.app
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app


@pytest.fixture()
def client(server):
    return server.test_client()

def test_create_post_should_work(client):
    # Arrange
    post = {"title": "Test title", "content": "Test content"}
    # Act
    response = client.post(f"http://localhost:5000/posts", json=post)
    # Assert
    assert response.status_code == 201

def test_get_post_should_work(client):
    # Arrange
    post = {"title": "Test title", "content": "Test content"}
    client.post(f"http://localhost:5000/posts", json=post)
    # Act
    response = client.get(f"http://localhost:5000/posts")
    # Assert
    assert response.status_code == 200
    assert response.json() == [{"title": "Test title", "content": "Test content"}]