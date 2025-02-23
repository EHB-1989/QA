from locust import HttpUser, task, between

class ProductSearchUser(HttpUser):
    wait_time = between(1, 2)  # Temps d'attente entre les requêtes

    @task
    def search_products(self):
        # Effectue une recherche pour des termes communs
        self.client.get("/search?query=phone")

    @task
    def search_products_rare(self):
        # Effectue une recherche pour des termes rares
        self.client.get("/search?query=abracadabra")
