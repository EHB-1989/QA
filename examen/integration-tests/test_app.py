#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   test_app.py
@Time    :   2025/02/23
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   None
'''

import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
    
    