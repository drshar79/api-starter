import requests


URL = "http://api.open-notify.org/astros.json"

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format
data = {
  "message": "success",
  "number": 3,
  "people": [
    {
      "name": "Andrew Morgan",
      "craft": "ISS"
    },
    {
      "name": "Oleg Skripochka",
      "craft": "ISS"
    },
    {
      "name": "Jessica Meir",
      "craft": "ISS"
    },
  ]
}

def choice():
    print(data["people"])
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
#print(res2)