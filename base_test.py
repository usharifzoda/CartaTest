#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unittest
from http_requests import SampleHTTPRequests

class BaseTest(unittest.TestCase):
    """@description: class to provide SetUp and TearDown as well as global vars
               @author: usharifzoda"""

    API_KEY = "002c3ceedee6bd9c6f5abbb7b476b0da"

    def setUp(self):
        self.api_requests = SampleHTTPRequests()

    def tearDown(self):
        print("API Tests are finished")

    if __name__ == '__main__':
        unittest.main(verbosity=2)