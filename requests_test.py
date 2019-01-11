#!/usr/bin/python

import requests

print(requests.__version__)

response = requests.get("http://www.google.com")
# print(dir(response))
print(response.text)
print(response.status_code)