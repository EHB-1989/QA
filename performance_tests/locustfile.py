from locust import HttpUser, task, between

# definition of a user class
class WebsiteUser(HttpUser):
    # define the wait time between tasks
    wait_time = between(1, 3)

    # define the tasks to be executed by the user
    @task
    def load_homepage(self):
        self.client.get("/")  # test the home page

    @task
    def load_about_page(self):
        self.client.get("/about")  # test the about page
