import requests
from flight_search import FlightSearch

class FlightData:
    def __init__(self):
        self.fight_search_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        self.headers={
                "Authorization" : f"Bearer {FlightSearch().token}",
            }

    def search_flights(self, or_code, dst_code, dpDate, rtnDate, lowest_price):
        params = {
            "originLocationCode":or_code,
            "destinationLocationCode":dst_code,
            "departureDate":dpDate.strftime("%Y-%m-%d"),
            "returnDate":rtnDate.strftime("%Y-%m-%d"),
            "adults":1,
            "nonStop":"true",
            "currencyCode":"GBP",
            "max":"10",
        }
        response = requests.get(self.fight_search_endpoint,params=params, headers=self.headers)
        response.raise_for_status()

        list = response.json()["data"]

        print(f"Searchin flight to {dst_code}...")

        if len(list) > 0:
            min = float(list[0]["price"]["grandTotal"])

            for offer in list:
                price = float(offer["price"]["grandTotal"])
                if price < min:
                    min = price

            print(f"{min}$")
        
            if min < lowest_price:
                print("HOT OFFER!")
        else:
            print("N/A")

