#!/bin/python3

import requests

URL = "https://letsrevolutionizetesting.com/challenge.json"

r = requests.get(url=URL)

data = r.json()

if 'follow' in data:
    print(requests.get(data['follow'].replace('challange?', 'challange.json?')))
else:
    print("Exception")

