#!/usr/bin/python3
"""sends a request to the URL and displays the value of the variable X-Request-Id."""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print(r.headers.get("X-Request-Id"))
