from locust import HttpUser, task, between

class WeatherUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://localhost:5000"

    @task
    def get_weather(self):
        self.client.get("/weather?city=Paris")
