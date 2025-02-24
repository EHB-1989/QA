from locust import HttpUser, task, between
from flask import jsonify

class APITestUser(HttpUser):
  wait_time = between(1, 3)

  @task(1)
  def get_api_data(self):
    self.client.get('/user/1')
