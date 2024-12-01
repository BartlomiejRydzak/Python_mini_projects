import requests
import os
from dotenv import load_dotenv

load_dotenv("./config.env")

class FlightSearch:
    def __init__(self):
            self.fight_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

            self.token = self.get_token()

            self.headers={
                "Authorization" : f"Bearer {self.token}",
            }
            
    def get_IATA_code(self, country):
        params = {
                "keyword":country,
                "max": "2",
                "include": "AIRPORTS",
            }
        
        response = requests.get(url=self.fight_endpoint,params=params, headers=self.headers)
        response.raise_for_status()

        data = response.json()
        return data["data"][0]["iataCode"]

    def get_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        body = {
            "grant_type":"client_credentials",
            "client_id": os.environ["API_KEY"],
            "client_secret":os.environ["API_SECRET"],
        }

        response = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=body)
        response.raise_for_status()
        return response.json()["access_token"]