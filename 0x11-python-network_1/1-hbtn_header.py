#!/usr/bin/python3
import requests.urllib
from sys import argv
"""Python script that takes in a URL, sends a request to the URL and displays"""


if __name__ == "__main__":
    r = requests.urllib.urlopen(argv[1])
    print(dict(r.headers).get('X-Request-Id'))
