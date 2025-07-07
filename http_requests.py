#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests


class SampleHTTPRequests(object):
    """@description: class with implementations of HTTP requests for test project
       @author: usharifzoda"""

    def __init__(self):
        self.http_requests = requests

    def get_request(self, api_url):

        # sending get request and returning the response as response object
        try:
            response = requests.get(url=api_url)
            return response
        except requests.exceptions.Timeout:
            raise RuntimeError("Failed to access endpoint due to timeout.")
        except requests.exceptions.TooManyRedirects:
            raise RuntimeError("Too many redirects occurred.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(
                "Critical issue found, respective stacktrace below: {0}".format(e)
            )
