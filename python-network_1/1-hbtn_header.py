#!/usr/bin/python3
"""get link from user"""
import sys
import urllib.request


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    request_id = response.headers.get("X-Request-Id")
print(request_id)
