import requests


URL = "http://api.open-notify.org/astros.json"

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format


def choice():
    print(res["people"])
    print("Would you like to see information about earthquakes?",
    "Yes or ",
    "No",
    ": ")
    ans = input()
    if ans== "Yes":
        print(res2)
URL2= "https://earthquake.usgs.gov/fdsnws/event/1/application.json"
res2 = requests.get(URL2)
res2 = res2.json()
choice()