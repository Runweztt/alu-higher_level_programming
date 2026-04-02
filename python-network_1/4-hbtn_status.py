#!/usr/bin/python3
"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
import requests
if __name__ == '__main__':
    res = requests.get('http://0.0.0.0:5050/status')
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
