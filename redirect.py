#!/bin/usr/env

import requests

url = "http://httbin.org/redirect-to"
payload = {"url":"http://www.bing.com"}

r = requests.get(url, params=payload)

print(r.text)
print("="*50)
print("Response Code: " + str(r.status_code))
print("="*50)

for x in r.history:
    print("="*50)
    print(str(x.status_code) + ":" + x.url)
    print("="*50)
