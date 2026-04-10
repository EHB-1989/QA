from locust import HttpUser, task, between


class BibliothequeUser(HttpUser):
    # Pas d'attente entre les requêtes pour maximiser la charge
    wait_time = between(0.1, 0.5)

    @task
    def get_user(self):
        # Tous les users demandent le même ID pour maximiser les hits de cache
        user_id = 1
        with self.client.get(f"/user/{user_id}", catch_response=True) as response:
            if response.status_code == 200:
                data = response.json()
                if "id" in data and "name" in data:
                    response.success()
                else:
                    response.failure("Réponse invalide : champs manquants")
            else:
                response.failure(f"Erreur HTTP : {response.status_code}")
