#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File    :   locustfile.py
@Time    :   2025/02/24 14:01:47
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   None
"""

from locust import HttpUser, task, between
import random 

class TestApp(HttpUser):
    wait_time = between(1, 2)
    host = "http://127.0.0.1:5000"

    def random_user_id(self):
        return random.randint(1, 100)

    @task 
    def get_user(self):
        data = self.client.get("/user/{}".format(self.random_user_id()))
        print(data.json())
