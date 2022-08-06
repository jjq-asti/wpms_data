import requests
import json



DATA_URL = "http://ec2-108-137-45-5.ap-southeast-3.compute.amazonaws.com/api/netmon/rfcdata/"





if __name__ == "__main__":
    res = requests.get(DATA_URL)
    data = res.json()
    with open("data.json", "w") as jsonfile:
        json.dump(data,jsonfile)
    
