import requests
def Choice():
    print("Do you want to find info about earthquakes(1), or amount of people in space(2)?")
    ans=input()
    if ans=="1":
        print(res2)
    elif ans=="2":
        print(res)
    else: 
        incorrect

def incorrect():
    print("That isn't one of your choices!")  
    Choice()


URL = "http://api.open-notify.org/astros.json"

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

URL2= "https://earthquake.usgs.gov/fdsnws/event/1/application.json"
res2 = requests.get(URL2)
res2=res2.json()
Choice()