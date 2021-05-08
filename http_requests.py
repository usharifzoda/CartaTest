#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import sys


class SampleHTTPRequests(object):
    """@description: class with implementations of HTTP requests for test project
       @author: usharifzoda"""

    def __init__(self):
        self.http_requests = requests

    def get_request(self, api_url):

        # sending get request and returning the response as response object
        try:
            r = requests.get(url=api_url)
        except requests.exceptions.Timeout:
            print("Failed to access endpoint due to timeout.")
        except requests.exceptions.TooManyRedirects:
            print("Too many redirects occurred.")
        except requests.exceptions.RequestException as e:
            print("Critical issue found, respective stacktrace below: {0}".format(e))
            sys.exit(1)

        return r