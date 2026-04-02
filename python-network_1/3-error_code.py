#!/usr/bin/python3
"""Script that takes a URL, sends request and handles HTTP errors."""
import sys
from urllib import request, error
if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as resq:
            print(resq.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
