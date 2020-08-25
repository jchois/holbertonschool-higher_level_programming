#!/usr/bin/python3
"""
script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    req = requests.get(url, auth=auth)
    try:
        print(req.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
