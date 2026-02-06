#!/usr/bin/python3
"""python requests fetching data"""
import requests


r = requests.get('https://intranet.hbtn.io/status')

print("Body response:")
print("\t- type:", type(r))
print("\t- content:", r.content)
