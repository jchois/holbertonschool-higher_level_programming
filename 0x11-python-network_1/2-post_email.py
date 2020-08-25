#!/usr/bin/python3
"""POST an email #0"""

import urllib.request
import urllib.parse
from sys import argv


if __name__ == '__main__':
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    url = argv[1]

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode())
