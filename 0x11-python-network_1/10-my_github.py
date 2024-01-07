#!/usr/bin/pyhton3
"""script that takes your Github credentials (username and password)."""


if __name__ == "__main__":
    import requests
    import sys
    url = "https://api.github.com/user"
    r = requests.get(url,
                     auth=requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(r.json().get("id"))
