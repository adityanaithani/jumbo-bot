import requests
import json

params = {
  'api_key': 'ceca995a-94d2-404c-954f-e136aef2cfa6',
  }

flights = 'http://airlabs.co/api/v9/flights'
flight_res = requests.get(flights, params)
flight_json = flight_res.json()['response']

airports = 'http://airlabs.co/api/v9/airports'
airport_res = requests.get(airports, params)
airport_json = airport_res.json()['response']

# gets flight data from flight number
def get_flight(flight_number):
    for flight in flight_json:
        if 'flight_iata' in flight:
            if flight['flight_iata'] == flight_number:
                return flight
    return "Flight not found"

def get_arrival(flight_number):
    flight = get_flight(flight_number)
    if flight == "Flight not found":
        return "Flight not found"
    else:
        for airport in airport_json:
            if airport['iata_code'] == flight['arr_iata']:
                return airport['name']
        return "Airport not found"

print(get_arrival('AA718'))