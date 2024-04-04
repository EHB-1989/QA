from locust import HttpUser, task, between

class GetUsersFromDB(HttpUser):
    wait_time = between(1, 2)
    
    @task
    def get_users(self):
        users = [self.client.get('/user/' + str(i)) for i in range(10)]
        