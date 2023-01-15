import requests

params = {
  'access_key': 'ec85ba11310ed78a1ba0040278d91402',
  'airline_iata': 'AA',
    }

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()

print(api_result, api_response)

