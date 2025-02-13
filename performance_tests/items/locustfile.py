from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)  # Attente aléatoire entre 1 et 3 secondes entre les requêtes

    @task(1)
    def get_home(self):
        """Test de la route d'accueil"""
        self.client.get("/")

    @task(2)
    def get_data(self):
        """ Test the data route """
        self.client.get("/api/data")

    @task(3)
    def post_item(self):
        """Test the item creation route"""
        item_data = {"name": "TestItem", "description": "Ceci est un test"}
        self.client.post("/api/items", json=item_data)

    @task(4)
    def simulate_long_processing(self):
        """Test the long processing simulation route"""
        self.client.get("/api/simulate_long_processing")
