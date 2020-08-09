#!/bin/usr/env

import requests

myheaders = {"user-agent":"Iphone 6"}
r = requests.post("http://httpbin.org/post", headers=myheaders)
#r = requests.post("http://httpbin.org/post", data={"name":"packt"})
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