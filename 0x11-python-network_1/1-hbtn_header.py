#!/usr/bin/python3
"""Script that takes in a URL, sends arequest to the URL."""
import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as url_req:
        print(url_req.headers.get('X-Request-Id'))
