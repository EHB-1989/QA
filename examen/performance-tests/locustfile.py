from locust import HttpUser, task, between
import json

class ApiTestUser(HttpUser):

    wait_time = between(1, 3) 

    @task(2)
    def get_posts(self):
        response = self.client.get("/posts")
        assert response.status_code == 200

    @task(1)
    def create_post(self):
        post_data = {
            "title": "Post de test",
            "content": "Contenu du post de test"
        }
        response = self.client.post("/posts", data=json.dumps(post_data), headers={"Content-Type": "application/json"})
        assert response.status_code == 201