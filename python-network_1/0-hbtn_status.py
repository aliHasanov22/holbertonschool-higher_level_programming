#!/usr/bin/python3
from urllib.request import urlopen
# pyhton fetches file


with urlopen("https://intranet.hbtn.io/status") as response:
    body = response.read()
print(body)
