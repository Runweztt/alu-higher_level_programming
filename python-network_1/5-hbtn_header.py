#!/usr/bin/python3
"""Script that takes a URL and displays the value of X-Request-Id header."""
import sys
import requests
if __name__ == '__main__':
    reqs = requests.get(sys.argv[1])
    print(reqs.headers.get("X-Request-Id"))
