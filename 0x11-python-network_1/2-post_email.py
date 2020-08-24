#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL."""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    email = parse.urlencode({"email": argv[2]}).encode()
    with request.urlopen(argv[1], email) as response:
        print(response.read().decode('utf-8'))
