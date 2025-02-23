from locust import HttpUser, task, between
from item import Item


class APITestUser(HttpUser):
    wait_time = between(
        1, 50
    )  # Les utilisateurs attendront entre 1 et 3 secondes entre les tâches

    @task
    def get_home(self):
        self.client.get("/")

    @task
    def test_add_item(self):
        Item = Item("Test Item", "Ceci est un article de test.")
        for i in range(10):
            self.client.post(
                "/api/items", json={"name": Item.name, "description": Item.description}
            )

    @task
    def test_get_items(self):
        self.client.get("/api/items")
        print("Items récupérés avec succès!")
    
    @task
    def test_simulate_long_processing(self):
        self.client.get("/api/simulate_long_processing")
        print("Traitement long terminé!")
    