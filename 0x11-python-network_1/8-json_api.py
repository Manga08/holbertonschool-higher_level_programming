#!/usr/bin/python3
"""Takes in a letter and sends a POST to http://0.0.0.0:5000/search_user."""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No responseult")
    except:
        print("Not a valid JSON")
