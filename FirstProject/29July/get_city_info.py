import requests

city ="Toronto"

api_url ="https://geocoding-api.open-meteo.com/v1/search"

params={
    "name":city,
    "count":1
}
response=requests.get(api_url, params=params)
print(response.text)