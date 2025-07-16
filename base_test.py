#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import unittest
from http_requests import SampleHTTPRequests

class BaseTest(unittest.TestCase):
    """@description: class to provide SetUp and TearDown as well as global vars
               @author: usharifzoda"""

    API_KEY = os.environ.get("WEATHER_API_KEY")

    if not API_KEY:
        raise EnvironmentError(
            "WEATHER_API_KEY environment variable is not set"
        )

    def setUp(self):
        self.api_requests = SampleHTTPRequests()

    def tearDown(self):
        print("API Tests are finished")

    if __name__ == '__main__':
        unittest.main(verbosity=2)