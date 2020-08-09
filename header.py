#!/bin/usr/env

import requests

r = requests.get("http://httpbin.org/ip")
print(r.url)
print("Status Code: ")
print("\t[-]" + str(r.status_code) + "\n")

print("Server Headers")
print("*"*50)
for x in r.headers:
    print("\t" + x + ":" + r.headers[x])
print("*"*50)
print("Content: \n")
print(r.text)