import requests
import json

params = {
    "api_key": "ceca995a-94d2-404c-954f-e136aef2cfa6",
}

flights = "http://airlabs.co/api/v9/flights"
flights_res = requests.get(flights, params)
flights_json = flights_res.json()["response"]

airports = "http://airlabs.co/api/v9/airports"
airport_res = requests.get(airports, params)
airport_json = airport_res.json()["response"]


# gets flight data from flight number
def get_flight(flight_number):
    for flight in flights_json:
        if "flight_iata" in flight:
            if flight["flight_iata"] == flight_number:
                return flight
    return "Flight not found"


# gets departure airport name from flight number
def get_departure(flight_number):
    flight = get_flight(flight_number)
    if flight == "Flight not found":
        return "Flight not found"
    else:
        for airport in airport_json:
            if airport["iata_code"] == flight["dep_iata"]:
                return airport["name"]
        return "Airport not found"


# gets arrival airport name from flight number
def get_arrival(flight_number):
    flight = get_flight(flight_number)
    if flight == "Flight not found":
        return "Flight not found"
    else:
        for airport in airport_json:
            if airport["iata_code"] == flight["arr_iata"]:
                return airport["name"]
        return "Airport not found"


# gets departure time from flight number
def get_departure_time(flight_number):
    flight = "https://airlabs.co/api/v9/flight?flight_iata=" + flight_number
    flight_res = requests.get(flight, params)
    if "response" in flight_res.json():
        flight_json = flight_res.json()["response"]
    else:
        return "No available time data"
    if "dep_time" in flight_json:
        return flight_json["dep_time"]
    else:
        return "Departure time not found"


# gets arrival time from flight number
def get_arrival_time(flight_number):
    flight = "https://airlabs.co/api/v9/flight?flight_iata=" + flight_number
    flight_res = requests.get(flight, params)
    if "response" in flight_res.json():
        flight_json = flight_res.json()["response"]
    else:
        return "No available time data"
    if "arr_time" in flight_json:
        return flight_json["arr_time"]
    else:
        return "Arrival time not found"
