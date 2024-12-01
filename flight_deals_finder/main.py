from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
import datetime as dt

flight_search = FlightSearch()
data_manager = DataManager()
flight_data = FlightData()

now = dt.datetime.now()
tomorrow = now + dt.timedelta(days=1)
in_six_months = now + dt.timedelta(days=6*30)

countries = data_manager.get_country_list()
for country in countries:

    if country["iataCode"] == "":
        iata = flight_search.get_IATA_code(country["city"].upper())
        data_manager.set_IATA_code(iata, country["id"])

    flight_data.search_flights("LON", country["iataCode"], tomorrow, in_six_months, country["lowestPrice"])