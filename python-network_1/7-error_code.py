#!/usr/bin/python3
"""Script that takes a URL and displays body or error code if >= 400."""
import sys
import requests
if __name__ == '__main__':
    url = sys.argv[1]
    reqs = requests.get(url)
    if reqs.status_code >= 400:
        print('Error code: {}'.format(reqs.status_code))
    else:
        print(reqs.text)
