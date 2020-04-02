import requests
import json

def get_country_language(country):
    url = "https://restcountries.eu/rest/v2/name/" + country
    #print(url)
    response = requests.get(url)
    #print(response.text) 
    data = json.loads(response.text)
    return data[0]["languages"][0]["name"]


