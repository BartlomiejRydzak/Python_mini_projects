import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.sheety_endpoint= "https://api.sheety.co/97c645de887f153dbd7238d80b614716/flightDeals/prices"

        self.auth = HTTPBasicAuth(os.environ["USERNAME"], os.environ["PASSWORD"])

    def get_country_list(self):
        response = requests.get(self.sheety_endpoint, auth=self.auth)
        response.raise_for_status()
        return response.json()["prices"]

    def set_IATA_code(self, iata, id):
        params= {
            "price": {
                "iataCode":iata,
            }

        }
        response = requests.put(self.sheety_endpoint+"/"+str(id), json=params, auth=self.auth)
        response.raise_for_status()
        print(response.json())