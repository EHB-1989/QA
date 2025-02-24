from locust import HttpUser, task, between

class ProductSearchUser(HttpUser):
    wait_time = between(1, 2)  # Temps d'attente entre les requêtes
    host = "http://localhost:5000"

    @task
    def search_products(self):
        # Effectue une recherche pour des termes communs
        data = self.client.get("/search?query=phone")
        print(data.json())

    @task
    def search_products_rare(self):
        # Effectue une recherche pour des termes rares
        data = self.client.get("/search?query=abracadabra")
        print(data.json())
