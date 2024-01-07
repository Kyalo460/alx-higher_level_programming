#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
