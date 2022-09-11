import requests
import json

BASE_URI = 'https://restcountries.eu/rest/v1'
QUERY_SEPARATOR = ','

class Country(object):

    def __str__(self):
        return u'{}'.format(self.name)

    def __init__(self, country_data):
        self.top_level_domain = country_data.get('topLevelDomain', None)
        self.alpha2_code = country_data.get('alpha2Code', None)
        self.alpha3_code = country_data.get('alpha3Code', None)
        self.currencies = country_data.get('currencies', None)
        self.capital = country_data.get('capital', None)
        self.calling_codes = country_data.get('callingCodes', None)
        self.alt_spellings = country_data.get('altSpellings', None)
        self.relevance = country_data.get('relevance', None)
        self.region = country_data.get('region', None)
        self.subregion = country_data.get('subregion', None)
        self.translations = country_data.get('translations', None)
        self.population = country_data.get('population', None)
        self.latlng = country_data.get('latlng', None)
        self.demonym = country_data.get('demonym', None)
        self.area = country_data.get('area', None)
        self.gini = country_data.get('gini', None)
        self.timezones = country_data.get('timezones', None)
        self.borders = country_data.get('borders', None)
        self.native_name = country_data.get('nativeName', None)
        self.name = country_data.get('name', None)
        self.numeric_code = country_data.get('numericCode', None)
        self.languages = country_data.get('languages', None)
        self.flag = country_data.get('flag', None)
        self.regional_blocs = country_data.get('regionalBlocs', None)
        self.cioc = country_data.get('cioc', None)

def get_country_list(resource, term=''):
	"""Takes a resource and a search term and return a list of countries or a country.
	:param resource - resource to create the URL
	:param term - search term provided by the user of this package
	:returns - either a Country object or a list of Countries
	"""
	uri = '{}{}/{}'.format(BASE_URI, resource, term)  # build URL
	print(uri)
	response = requests.get(uri)
	if response.status_code == 200:
	    result_list = []
	    data = json.loads(response.text)  # parse json to dict
	    if type(data) == list:
		    for country_data in data:  # in case it is a list create python list with country instances
		        country = Country(country_data)
		        result_list.append(country)
	    else:
		    return Country(data)
	    return result_list
	elif response.status_code == 404:
	    raise requests.exceptions.InvalidURL
	else:
	    raise requests.exceptions.RequestException

if __name__ == "__main__":

    country_list = get_country_list('/name', 'France')
    if(type(country_list) == list):
        for country in country_list:
            print(country.languages)
