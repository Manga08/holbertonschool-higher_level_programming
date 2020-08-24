#!/usr/bin/python3
"""Use the Github API to list the 10 most recent commits from rails rails."""
import requests
from sys import argv


if __name__ == '__main__':
    resp = requests.get('https://api.github.com/repos/{}/{}/commits'
                        .format(argv[2], argv[1]))
    for commit in resp.json()[0:10]:
        print('{}: {}'.format(commit.get('sha'), commit.get('commit')
                              .get('author').get('name')))
