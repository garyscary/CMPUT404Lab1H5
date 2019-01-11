#!/usr/bin/python

import requests

print(requests.__version__)

response = requests.get("https://raw.githubusercontent.com/garyscary/CMPUT404Lab1H5/master/requests_test.py")
# print(dir(response))
print(response.text)
# print(response.status_code)