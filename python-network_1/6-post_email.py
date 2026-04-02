#!/usr/bin/python3
"""Script that takes a URL and email, sends POST request and displays body."""
import sys
import requests
if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    reqs = requests.post(url, data=value)
    print(reqs.text)
