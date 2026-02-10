#!/usr/bin/python3
""" takes 2 arguments in order to solve this challenge"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {"per_page": 10}
    r = requests.get(url, params=params)
    commits = r.json()
    for c in commits[:10]:
        sha = c.get("sha", "")
        name = c.get("commit", {}).get("author", {}).get("name", "")
        print(f"{sha}: {name}")
