import requests


URL = "http://api.open-notify.org/astros.json"

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

print(res)