#!/usr/bin/python3
"""Takes in a URL and an email address, sends a POST."""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
