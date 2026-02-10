#!/usr/bin/python3
"""Advance task getting multiple github"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {"per_page": 10}
    resp = requests.get(url, params=params)
    commits = resp.json()
    for c in commits[:10]:
        sha = c.get("sha", "")
        # Preferred: GitHub user display name if available
        author_name = ""
        if c.get("author") and c["author"].get("login"):
            author_name = c["author"]["login"]
        else:
            author_name = (c.get("commit", {})
                             .get("author", {})
                             .get("name", ""))
        print(f"{sha}: {author_name}")
