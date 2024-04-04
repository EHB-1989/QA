from locust import HttpUser, task, between

class WeatherAppUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_weather_data(self):
        city = "Paris" 
        self.client.get(f"/weather?city={city}", name="/weather")