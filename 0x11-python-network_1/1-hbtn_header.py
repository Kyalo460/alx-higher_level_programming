#!/usr/bin/python3
import requests
from sys import argv
"""Python script that takes in a URL, sends a request to the URL and displays"""


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
