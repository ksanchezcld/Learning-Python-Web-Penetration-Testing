
import requests

url = "http://httpbin.org/html"
req = requests.get(url)
print("Response Code: " + str(req.status_code))